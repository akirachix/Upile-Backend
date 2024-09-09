from django.db import models 
# from missing_persons.models import MissingPerson  


class NextOfKin(models.Model):
    """
    Model representing a next of kin for a missing person. 
    This class includes fields for storing essential information such as 
    the next of kin's ID, names, address, relationship to the missing person, 
    and contact details. The model is designed to establish a connection 
    with the MissingPerson model, facilitating the management of 
    next of kin information in the context of missing persons cases.
    """
    next_of_kin_id = models.SmallIntegerField(primary_key=True)  
    # missing_person_id = models.ForeignKey(MissingPerson, on_delete=models.CASCADE)  
    first_name = models.CharField(max_length=50)  
    last_name = models.CharField(max_length=50)  
    address = models.CharField(max_length=50, default='Unknown')
    relationship = models.CharField(max_length=50)
    contact = models.CharField(max_length=15)  
    alternative_contact = models.CharField(max_length=15, default='Unknown')
      

    def __str__(self):
        """String representation of the NextOfKin instance"""
        return f"{self.first_name} ({self.last_name})"