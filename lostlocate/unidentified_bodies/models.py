from django.db import models  # Importing the models module from Django
from django.utils import timezone
# from mortuary_staff.models import MortuaryStaff  # Importing the MortuaryStaff model

# Create your models here.

class UnidentifiedBody(models.Model):
    SKIN_COLOR_CHOICES =[
        ('light_skinned', 'Light Skinned'),
        ('dark_skinned', 'Dark Skinned')
    ]

    # Defining the primary key for the UnidentifiedBody model
    body_id = models.SmallIntegerField(primary_key=True)  
    # Foreign key linking to the MortuaryStaff model, with cascade delete behavior
    # mortuary_staff_id = models.ForeignKey(MortuaryStaff, on_delete=models.CASCADE)  
    # Field to store the name of the unidentified body
    name = models.CharField(max_length=50)  
    # Field to store the gender of the unidentified body
    gender = models.CharField(max_length=50)  
    # Field to store the location where the unidentified body was found
    location = models.CharField(max_length=50)  
    # Field to store the skin color of the unidentified body
    skin_color = models.CharField(max_length=50,choices=SKIN_COLOR_CHOICES,default='dark_skinned')
    # Field to store the weight of the unidentified body
    weight = models.FloatField()  
    # Field to store the height of the unidentified body
    height = models.FloatField()  
    # Field to store any body marks or distinguishing features of the unidentified body
    body_marks = models.TextField()  
    # Field to store the date and time when the unidentified body was reported
    reporting_date = models.DateTimeField()  
    # Field to store the clothes worn by the unidentified body
    clothes_worn = models.TextField()  
    # Field to store the hair color of the unidentified body
    hair_color = models.CharField(max_length=50) 
    # Date and time when the record was created  
    created_at = models.DateTimeField(default=timezone.now) 


    def __str__(self):
        # String representation of the UnidentifiedBody instance
        return self.name