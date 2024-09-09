from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils import timezone
import uuid
# CustomUser Model
class CustomUser(models.Model):
        # Choices for the user role
    ROLE_CHOICES = [
        ('police_officer', 'Police Officer'),
        ('mortuary_staff', 'Mortuary Staff'),
    ]
    
    first_name= models.CharField(max_length=20)
    # Phone number field with unique constraint
    phone_number = models.CharField(max_length=15, unique=True)
    last_name = models.CharField(max_length = 20)
    # Role field with predefined choices and a default value
    role = models.CharField(max_length=30, choices=ROLE_CHOICES, default='police_officer')
    email = models.EmailField(unique=True)
    def save(self, *args, **kwargs):
        # Hash the password if it does not start with specific prefixes
        if not self.password.startswith(('po1234_', 'mo1234')):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.username
# VerificationCode Model
class RegistrationCode(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Corrected field name
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(default=timezone.now)
    expires_at = models.DateTimeField()
    def is_expired(self):
        return timezone.now() > self.expires_at