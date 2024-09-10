from django.db import models
from django.utils import timezone
# from mortuary_staff.models import MortuaryStaff  

# Create your models here.

class UnidentifiedBody(models.Model):
    """
    Model representing an unidentified body in a mortuary context. 
    This class includes fields for storing essential details such as 
    the body’s ID, name, gender, location of discovery, physical attributes 
    (skin color, weight, height, hair color), distinguishing features, 
    clothing, and reporting information. It is designed to facilitate 
    the management and identification process of unidentified bodies, 
    with a potential link to mortuary staff for further processing.
    """
    SKIN_COLOR_CHOICES = [
        ('light_skinned', 'Light Skinned'),
        ('dark_skinned', 'Dark Skinned')
    ]

    body_id = models.SmallIntegerField(primary_key=True)  
    # mortuary_staff_id = models.ForeignKey(MortuaryStaff, on_delete=models.CASCADE)  
    name = models.CharField(max_length=50)  
    gender = models.CharField(max_length=50)  
    location = models.CharField(max_length=50)  
    skin_color = models.CharField(max_length=50, choices=SKIN_COLOR_CHOICES, default='dark_skinned')
    weight = models.FloatField()  
    height = models.FloatField()  
    body_marks = models.TextField()  
    reporting_date = models.DateTimeField()  
    clothes_worn = models.TextField()  
    hair_color = models.CharField(max_length=50) 
    created_at = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        """String representation of the UnidentifiedBody instance"""
        return self.name
