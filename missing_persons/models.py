from django.db import models
from django.core.exceptions import ValidationError
from police.models import PoliceOfficer

class MissingPerson(models.Model):
    """Attributes for the missing persons added by the police officers"""
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    SKIN_COLOR_CHOICES = [
        ('light_skinned', 'Light Skinned'),
        ('dark_skinned', 'Dark Skinned')
    ]

    EYE_COLOR_CHOICES = [
        ('black', 'Black'),
        ('brown', 'Brown')
    ]

    id = models.AutoField(primary_key=True)
    officer_id = models.ForeignKey(PoliceOfficer, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100, default='Unknown')
    age = models.SmallIntegerField()
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default='other')
    contact = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.FloatField()
    hair_color = models.CharField(max_length=50)
    eye_color = models.CharField(max_length=50, choices=EYE_COLOR_CHOICES, default='black')
    skin_color = models.CharField(max_length=50, choices=SKIN_COLOR_CHOICES, default='dark_skinned')
    missing_date = models.DateField()
    location = models.CharField(max_length=50)
    clothes_worn = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Return the full name of the missing person
        return f"{self.first_name} {self.last_name}"

    def clean(self):
        # Ensure first_name is not just whitespace
        if not self.first_name.strip():
            raise ValidationError('First name cannot be blank or whitespace')

        # Additional validations
        if self.age < 0:
            raise ValidationError('Age cannot be negative')

    def save(self, *args, **kwargs):
        self.clean()  # Ensure custom validation is applied
        super().save(*args, **kwargs)
