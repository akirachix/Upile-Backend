
from django.db import models
from django.contrib.auth.models import User  # Import the built-in User model
# from .models import Mortuary  # Import the Mortuary model

class MortuaryStaff(models.Model):
    """
    Model representing staff members working at a mortuary.
    """
    staff_id = models.SmallIntegerField(primary_key=True)
    # The unique identifier for the staff member. Used as the primary key.
    
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # ForeignKey relationship to the built-in User model. Represents the user associated with the staff member.
    
    position = models.CharField(max_length=30)
    # The position or role of the staff member within the mortuary. Limited to 30 characters.
    
    contact = models.CharField(max_length=15)
    # Contact number of the staff member. Limited to 15 characters.
    
    # mortuary_id = models.ForeignKey(Mortuary, on_delete=models.CASCADE)
    # ForeignKey relationship to the Mortuary model. Represents the mortuary where the staff member works.
    
    generated_code = models.CharField(max_length=30)
    # A code generated for the staff member. Limited to 30 characters.

    def __str__(self):
        """
        String representation of the MortuaryStaff object.
        """
        return f"Staff {self.staff_id} - {self.position}"
