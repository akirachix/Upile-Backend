import logging
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import LoginSerializer, VerifyOtpSerializer
from django.core.cache import cache
import random
import requests
import re
from django.conf import settings

# Set up logging for the module
logger = logging.getLogger(__name__)

# Function to generate a 6-digit OTP (One-Time Password)
def generate_otp():
    return str(random.randint(100000, 999999))

# Function to send OTP via SMS using the Leopard SMS API
def send_otp(phone_number, otp):
    # Set up the necessary headers for the API request
    headers = {
        'Authorization': f'Basic {settings.SMS_LEOPARD_ACCESS_TOKEN}',
        'Content-Type': 'application/json',
    }
    
    # Prepare the payload for the API call, including the OTP message
    payload = {
        "source": "AkiraChix",
        "message": f'Your OTP code is {otp}',
        "destination": [{"number": phone_number}]
    }

    try:
        # Send the OTP via POST request
        response = requests.post(settings.SMS_LEOPARD_API_URL, json=payload, headers=headers)
        
        # Checks if the response from the SMS API was successful
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"Failed to send OTP: {response.status_code} - {response.text}")
            return None
    except requests.RequestException as e:
        # Log any exceptions during the API request
        logger.error(f"Request exception occurred: {e}")
        return None

# Function to validate phone numbers (Kenya format), converting it to international format
def validate_phone_number(phone_number):
    # Regular expression pattern to match valid Kenyan phone numbers starting with '0'
    pattern = re.compile(r'^0[1-9]\d{8}$')
    
    # If the phone number matches the pattern, convert to international format
    if pattern.match(phone_number):
        return '+254' + phone_number[1:]  # Convert '0' to '+254' for international format
    return None

# API view for registering a user and sending OTP to their phone number
@api_view(['POST'])
def login_user(request):
    """Handle user registration by sending an OTP."""
    try:
        serializer = LoginSerializer(data=request.data)
        
        # Validate the phone number from the request
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            formatted_number = validate_phone_number(phone_number)
            
            # If the phone number is invalid, return a bad request response
            if not formatted_number:
                return Response({'error': 'Invalid phone number format. Please use the format: 0723456789.'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Generate a 6-digit OTP
            otp = generate_otp()
            
            # Send the OTP to the user's phone number
            response = send_otp(formatted_number, otp)
            
            # If the OTP was successfully sent, store the OTP in the cache and create a user record
            if response and response.get('status') == 'success':
                cache.set(formatted_number, otp, timeout=300)  # Cache the OTP for 5 minutes (300 seconds)
                
                # Get or create a user with the provided phone number
                user, created = CustomUser.objects.get_or_create(phone_number=formatted_number)
                user.generated_code = otp  # Store the OTP for future verification
                user.is_active = False  # Set user to inactive until OTP is verified
                user.save()
                
                return Response({'message': 'OTP sent to your phone number.'}, status=status.HTTP_200_OK)
            else:
                # Handle OTP sending failure
                return Response({'error': 'Failed to send OTP. Please try again.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        # Log any unexpected errors
        logger.error(f"Error in login_user view: {e}")
        return Response({'error': 'An unexpected error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# API view for verifying OTP and completing user registration
@api_view(['POST'])
def verify_otp(request):
    """Verify the OTP submitted by the user."""
    try:
        serializer = VerifyOtpSerializer(data=request.data)
        
        # Validate the input data (phone number, OTP, password)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            otp = serializer.validated_data['otp']
            password = serializer.validated_data.get('password')  # Password is optional
            
            # Format the phone number to international format
            formatted_number = validate_phone_number(phone_number)
            
            # If the phone number format is invalid, return a bad request response
            if not formatted_number:
                return Response({'error': 'Invalid phone number format. Please use the format: 0723456789.'}, status=status.HTTP_400_BAD_REQUEST)
            
            # Retrievinf the cached OTP and check if it matches the one provided
            cached_otp = cache.get(formatted_number)
            if cached_otp and cached_otp == otp:
                # Get the user by phone number and mark them as active
                user = CustomUser.objects.get(phone_number=formatted_number)
                user.is_active = True
                
                # If a password is provided, set the user's password
                if password:
                    user.set_password(password)
                user.save()
                
                return Response({'message': 'User registered successfully.'}, status=status.HTTP_201_CREATED)
            else:
                # If the OTP or phone number is invalid, return a bad request response
                return Response({'error': 'Invalid OTP or phone number.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        # Log any unexpected errors
        logger.error(f"Error in verify_otp view: {e}")
        return Response({'error': 'An unexpected error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

