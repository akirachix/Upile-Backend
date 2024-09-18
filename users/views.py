import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser, RegistrationCode
from .serializers import LoginSerializer, VerifyOtpSerializer
from django.core.cache import cache
import random
import requests
import re
from django.contrib.auth import authenticate, login
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

logger = logging.getLogger(__name__)


"""Function to generate a 6-digit OTP"""
def generate_otp():
    return str(random.randint(100000, 999999))


"""Function to send OTP via SMS using the Leopard SMS API"""
def send_otp(phone_number, otp):
    headers = {
        "Authorization": f"Basic {settings.SMS_LEOPARD_ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }

    payload = {
        "source": "AkiraChix",
        "message": f"Your OTP code is {otp}",
        "destination": [{"number": phone_number}],
    }

    try:
        response = requests.post(
            settings.SMS_LEOPARD_API_URL, json=payload, headers=headers
        )
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(
                f"Failed to send OTP: {response.status_code} - {response.text}"
            )
            return None
    except requests.RequestException as e:
        logger.error(f"Request exception occurred: {e}")
        return None

"""Function to validate phone numbers (Kenya format)"""
def validate_phone_number(phone_number):
    pattern = re.compile(r"^0[1-9]\d{8}$")
    if pattern.match(phone_number):
        return "+254" + phone_number[1:]
    return None


"""API view for registering a user and sending OTP to their phone number"""
@api_view(["POST"])
def login_user(request):
    try:
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data["phone_number"]
            formatted_number = validate_phone_number(phone_number)
            if not formatted_number:
                return Response(
                    {"error": "Invalid phone number format. Use: 0723456789."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            otp = generate_otp()
            response = send_otp(formatted_number, otp)

            if response and response.get("status") == "success":
                cache.set(formatted_number, otp, timeout=300)
                user, created = CustomUser.objects.get_or_create(
                    phone_number=formatted_number
                )
                user.generated_code = otp
                user.is_active = False
                user.save()

                return Response(
                    {"message": "OTP sent to your phone number."},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"error": "Failed to send OTP. Please try again."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.error(f"Error in login_user: {e}")
        return Response(
            {"error": "An unexpected error occurred."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


"""API view for verifying OTP and completing user registration"""
@api_view(["POST"])
def verify_otp(request):
    try:
        serializer = VerifyOtpSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data["phone_number"]
            otp = serializer.validated_data["otp"]

            formatted_number = validate_phone_number(phone_number)
            if not formatted_number:
                return Response(
                    {"error": "Invalid phone number format. Use: 0723456789."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            cached_otp = cache.get(formatted_number)
            if cached_otp and cached_otp == otp:
                user = CustomUser.objects.get(phone_number=formatted_number)
                user.is_active = True
                user.save()

                return Response(
                    {"message": "User registered successfully."},
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {"error": "Invalid OTP or phone number."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.error(f"Err0or in verify_otp: {e}")
        return Response(
            {"error": "An unexpected error occurred."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


"""API for generating and sending a verification code via email (user registration)"""
def generate_short_code(role):
    code = random.randint(1111, 9999)
    prefix = "po" if role == "police" else "mo"
    return prefix + str(code)


@api_view(["POST"])
def user_register(request, length=6):
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    role = request.data.get("role")
    phone_number = request.data.get("phone_number")
    email = request.data.get("email")
    username = request.data.get("username")


    existing_user = CustomUser.objects.filter(email=email, username=username)
    if existing_user:
        return Response({"message":"User already exists"})
    else:
        user = CustomUser.objects.create(
            username = username,
            first_name=first_name,
            last_name=last_name,
            role=role,
            phone_number=phone_number,
            email=email,
            
        )

        short_code = generate_short_code(role)

        code = RegistrationCode.objects.create(
            user=user,
            code=short_code,
            created_at=timezone.now(),
        )

        subject = "Your Registration Code"
        message = f"Your registration code is {short_code}."
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]  # Ensure this is a list of strings

        try:
            send_mail(subject, message, from_email, recipient_list)
            return Response(
                {"message": "Verification code sent successfully."},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            logger.error(f"Failed to send email: {e}")
            return Response(
                {"error": f"Failed to send email: {e}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


"""API for verifying the email verification code"""
@api_view(["POST"])
@login_required
def verify_code(request):
    
    user = CustomUser(
            code= code,
            phone_number=phone_number,
        )
    try:
        code = request.data.get("code")
        phone_number = request.data.get("phone_number")

        verification_code = RegistrationCode.objects.get(
            code=code, phone_number=request.phone_number
        )
        if user.get("phone_number") != phone_number:
            return Response(
                {"error": "Phone number does not match."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not verification_code.is_expired():
            login(request, verification_code.user)
            return Response(
                {"message": "Verification successful."}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"error": "Code expired"}, status=status.HTTP_400_BAD_REQUEST
            )
    except RegistrationCode.DoesNotExist:
        return Response({"error": "Invalid code"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.error(f"Error in verify_code: {e}")
        return Response(
            {"error": "An unexpected error occurred."},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


