from django.db import models
from django.utils import timezone
# from police.models import PoliceOfficer

# Create your models here.
class MissingPerson(models.Model):
    # Choices for the gender field
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
    
    # Primary key for the model, using a small integer field
    missing_person_id = models.SmallIntegerField(primary_key=True)

    # officer_id = models.ForeignKey(PoliceOfficer)
    
    # Name of the missing person
    first_name = models.CharField(max_length=50)

    last_name = models.CharField(max_length=100, default='Unknown') 
    
    # Age of the missing person
    age = models.SmallIntegerField()
    
    # Gender of the missing person with predefined choices and a default value
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, default='other')
    
    # Contact information for the missing person
    contact = models.CharField(max_length=50)
    
    # Image of the missing person
    image = models.ImageField(upload_to='missing_persons/')
    
    # Height of the missing person (in meters or other units)
    height = models.FloatField()
    
    # Weight of the missing person (in kilograms or other units)
    weight = models.FloatField()
    
    # Hair color of the missing person
    hair_color = models.CharField(max_length=50)
    
    # Eye color of the missing person
    eye_color = models.CharField(max_length=50, choices=EYE_COLOR_CHOICES,default='black')
    
    # Skin color of the missing person
    skin_color = models.CharField(max_length=50,choices=SKIN_COLOR_CHOICES,default='dark_skinned')
    
    # Date and time when the person went missing
    missing_date = models.DateTimeField()
    
    # Location where the person was last seen or went missing
    location = models.CharField(max_length=50)
    
    # Description of the clothes the missing person was wearing
    clothes_worn = models.TextField()

    # Date and time when the record was created
    created_at = models.DateTimeField(default=timezone.now)    
    def __str__(self):
        # String representation of the MissingPerson instance, showing the name
        return f"{self.first_name} {self.last_name}"