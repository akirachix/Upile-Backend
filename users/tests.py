# from django.urls import reverse
# from rest_framework.test import APITestCase
# from rest_framework import status
# from django.core.cache import cache
# from users.models import CustomUser, RegistrationCode
# from unittest.mock import patch
# from django.utils import timezone
# class UserTests(APITestCase):
#     def setUp(self):
#         self.valid_phone_number = "0712345678"
#         self.invalid_phone_number = "07123456"
#         self.valid_otp = "123456"
#         self.invalid_otp = "999999"
#         self.valid_code = "mo1234"
#         self.valid_email = "test@example.com"
#         self.valid_role = "citizen"
#         self.valid_username = "hannah"
#         self.user_data = {
#             "first_name": "John",
#             "last_name": "Doe",
#             "role": self.valid_role,
#             "phone_number": self.valid_phone_number,
#             "email": self.valid_email,
#             "username":self.valid_username
#         }
#     # Test login_user endpoint
#     @patch('users.views.send_otp')
#     def test_login_user_valid(self, mock_send_otp):
#         mock_send_otp.return_value = {"status": "success"}
#         response = self.client.post(reverse('login'), {"phone_number": self.valid_phone_number})
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn("OTP sent to your phone number.", response.data["message"])
#     def test_login_user_invalid_phone(self):
#         response = self.client.post(reverse('login'), {"phone_number": self.invalid_phone_number})
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertIn("Invalid phone number format", response.data["error"])
#     # Test verify_otp endpoint
#     def test_verify_otp_valid(self):
#         # Simulate OTP in cache
#         formatted_phone = "+254712345678"
#         cache.set(formatted_phone, self.valid_otp, timeout=300)
#         response = self.client.post(reverse('verify_otp'), {
#             "phone_number": self.valid_phone_number,
#             "otp": self.valid_otp
#         })
#     @patch('django.core.mail.send_mail')
#     def test_user_register_valid(self, mock_send_mail):
#         mock_send_mail.return_value = 1
#         response = self.client.post(reverse('register'), self.user_data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn("Verification code sent successfully.", response.data["message"])
 
#     def test_verify_code_valid(self):
#         user = CustomUser.objects.create(
#             first_name="John",
#             last_name="Doe",
#             phone_number=self.valid_phone_number,
#             email=self.valid_email,
#             role=self.valid_role,
#             username= self.valid_username
#         )
#         RegistrationCode.objects.create(user=user, code=self.valid_code, created_at=timezone.now())
#         one = RegistrationCode.objects.filter(user=user)
#         response = self.client.post(reverse('verify_code'), {
#             "code": self.valid_code,
#             "phone_number": self.valid_phone_number
#         })



from django.test import TestCase
from django.utils import timezone
from .models import CustomUser, RegistrationCode

class CustomUserTestCase(TestCase):
    def setUp(self):
        """Create a user for testing."""
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='testpass',
            phone_number='1234567890',
        )

    def test_user_creation(self):
        """Test that a user is created successfully and generated_code is set."""
        self.assertIsNotNone(self.user.generated_code)
        self.assertEqual(CustomUser.objects.count(), 1)

    def test_generate_code(self):
        """Test the generate_code method."""
        code = self.user.generate_code()
        self.assertEqual(len(code), 6)
        self.assertTrue(code.isdigit())

    def test_user_role_permissions(self):
        """Test the permissions based on user role."""
        self.user.role = 'police_officer'
        self.assertTrue(self.user.has_permission('view_missing'))
        self.assertFalse(self.user.has_permission('add_unidentified_body'))

        self.user.role = 'mortuary_staff'
        self.assertTrue(self.user.has_permission('add_unidentified_body'))
        self.assertFalse(self.user.has_permission('update_missing'))

    def test_count_by_role(self):
        """Test counting users by role."""
        CustomUser.objects.create_user(username='police1', password='testpass', phone_number='1234567891', role='police_officer')
        CustomUser.objects.create_user(username='mortuary1', password='testpass', phone_number='1234567892', role='mortuary_staff')
        self.assertEqual(CustomUser.count_by_role('police_officer'), 2)
        self.assertEqual(CustomUser.count_by_role('mortuary_staff'), 1)

    def test_user_creation_with_duplicate_phone(self):
        """Test creating a user with a duplicate phone number."""
        with self.assertRaises(Exception):
            CustomUser.objects.create_user(
                username='testuser2',
                password='testpass',
                phone_number='1234567890'
            )

    def test_user_role_permissions_invalid_permission(self):
        """Test checking for an invalid permission."""
        self.user.role = 'police_officer'
        self.assertFalse(self.user.has_permission('non_existent_permission'))

    def test_generate_code_invalid_length(self):
        """Test the generate_code method if it returns an invalid length."""
        code = self.user.generate_code()
        self.assertNotEqual(len(code), 5)  # Ensuring it's not 5

class RegistrationCodeTestCase(TestCase):
    def setUp(self):
        """Create a user and registration code for testing."""
        self.user = CustomUser.objects.create_user(
            username='testuser',
            password='testpass',
            phone_number='1234567890',
        )
        self.registration_code = RegistrationCode.objects.create(
            user=self.user,
            code='123456',
            expires_at=timezone.now() + timezone.timedelta(hours=1)
        )


    def test_registration_code_without_expiration(self):
        """Test creating a registration code without expiration."""
        registration_code = RegistrationCode.objects.create(
            user=self.user,
            code='654321',
            expires_at=None
        )
        self.assertIsNone(registration_code.expires_at)
