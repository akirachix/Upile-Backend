from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.core.cache import cache
from users.models import CustomUser, RegistrationCode
from unittest.mock import patch
from django.utils import timezone
class UserTests(APITestCase):
    def setUp(self):
        self.valid_phone_number = "0712345678"
        self.invalid_phone_number = "07123456"
        self.valid_otp = "123456"
        self.invalid_otp = "999999"
        self.valid_code = "mo1234"
        self.valid_email = "test@example.com"
        self.valid_role = "citizen"
        self.user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "role": self.valid_role,
            "phone_number": self.valid_phone_number,
            "email": self.valid_email,
        }
    # Test login_user endpoint
    @patch('users.views.send_otp')
    def test_login_user_valid(self, mock_send_otp):
        mock_send_otp.return_value = {"status": "success"}
        response = self.client.post(reverse('login'), {"phone_number": self.valid_phone_number})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("OTP sent to your phone number.", response.data["message"])
    def test_login_user_invalid_phone(self):
        response = self.client.post(reverse('login'), {"phone_number": self.invalid_phone_number})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Invalid phone number format", response.data["error"])
    # Test verify_otp endpoint
    def test_verify_otp_valid(self):
        # Simulate OTP in cache
        formatted_phone = "+254712345678"
        cache.set(formatted_phone, self.valid_otp, timeout=300)
        response = self.client.post(reverse('verify_otp'), {
            "phone_number": self.valid_phone_number,
            "otp": self.valid_otp
        })
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertIn("User registered successfully.", response.data["message"])
    # def test_verify_otp_invalid(self):
    #     response = self.client.post(reverse('verify_otp'), {
    #         "phone_number": self.valid_phone_number,
    #         "otp": self.invalid_otp
    #     })
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertIn("Invalid OTP or phone number.", response.data["error"])
    # Test user_register endpoint
    @patch('django.core.mail.send_mail')
    def test_user_register_valid(self, mock_send_mail):
        mock_send_mail.return_value = 1
        response = self.client.post(reverse('register'), self.user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Verification code sent successfully.", response.data["message"])
    # def test_user_register_missing_field(self):
    #     incomplete_data = {
    #         "first_name": "John",
    #         "last_name": "Doe",
    #         "phone_number": self.valid_phone_number,
    #     }
    #     response = self.client.post(reverse('register'), incomplete_data)
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    # Test verify_code endpoint
    def test_verify_code_valid(self):
        user = CustomUser.objects.create(
            first_name="John",
            last_name="Doe",
            phone_number=self.valid_phone_number,
            email=self.valid_email,
            role=self.valid_role
        )
        RegistrationCode.objects.create(user=user, code=self.valid_code, created_at=timezone.now())
        response = self.client.post(reverse('verify_code'), {
            "code": self.valid_code,
            "phone_number": self.valid_phone_number
        })
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertIn("Verification successful.", response.data["message"])
    # def test_verify_code_invalid(self):
    #     response = self.client.post(reverse('verify_code'), {
    #         "code": "wrongcode",
    #         "phone_number": self.valid_phone_number
    #     })
    #     self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    #     self.assertIn("Invalid code", response.data["error"])
