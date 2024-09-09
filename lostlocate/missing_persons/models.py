from django.db import models
from django.utils import timezone
# from police.models import PoliceOfficer

# Create your models here.
class MissingPerson(models.Model):
    """Attribute for the missing persons added by the police officers"""
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    SKIN_COLOR_CHOICES =[
        ('light_skinned', 'Light Skinned'),
        ('dark_skinned', 'Dark Skinned')
    ]
    EYE_COLOR_CHOICES =[
        ('black', 'BLACK'),
        ('brown', 'BROWN')
    ]
    missing_person_id = models.SmallIntegerField(primary_key=True)
    # officer_id = models.ForeignKey(PoliceOfficer)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100, default='Unknown') 
    age = models.SmallIntegerField()
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default='other')
    contact = models.CharField(max_length=50)
    image = models.ImageField(upload_to='missing_persons/')
    height = models.FloatField()
    weight = models.FloatField()
    hair_color = models.CharField(max_length=50)
    eye_color = models.CharField(max_length=50, choices=EYE_COLOR_CHOICES,default='black')
    skin_color = models.CharField(max_length=50,choices=SKIN_COLOR_CHOICES,default='dark_skinned')
    missing_date = models.DateTimeField()
    location = models.CharField(max_length=50)
    clothes_worn = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)    
    def __str__(self):
        # String representation of the MissingPerson instance, showing the name
        return f"{self.first_name} {self.last_name}"