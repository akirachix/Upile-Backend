from django.db import models  # Importing the models module from Django
# from missing_persons.models import MissingPerson  # Importing the MissingPerson model

# Create your models here.

class NextOfKin(models.Model):
    # Defining the primary key for the NextOfKin model
    next_of_kin_id = models.SmallIntegerField(primary_key=True)  
    # Foreign key linking to the MissingPerson model, with cascade delete behavior
    # missing_person_id = models.ForeignKey(MissingPerson, on_delete=models.CASCADE)  
    # Field to store the first name of the next of kin
    first_name = models.CharField(max_length=50)  
    # Field to store the last name of the next of kin
    last_name = models.CharField(max_length=50)  
    # Field to store the location address of the next of kin
    address = models.CharField(max_length=50, default='Unknown')
    # Field to store the relationship of the next of kin to the missing person
    relationship = models.CharField(max_length=50)
    # Field to store the contact number of the next of kin
    contact = models.CharField(max_length=15)  
    # Field to store the alternative contact number of the next of kin
    alternative_contact = models.CharField(max_length=15, default='Unknown')
      

    def __str__(self):
        # String representation of the NextOfKin instance
        return f"{self.first_name} ({self.last_name})"