
from django.db import models
from django.contrib.auth.models import User  # Import the built-in User model
# from .models import Mortuary  """Import the Mortuary model"""

class MortuaryStaff(models.Model):
    """
    Model representing staff members working at a mortuary.
    """
    staff_id = models.SmallIntegerField(primary_key=True)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=30)
    contact = models.CharField(max_length=15)
     # mortuary_id = models.ForeignKey(Mortuary, on_delete=models.CASCADE)
    generated_code = models.CharField(max_length=30)

    def __str__(self):
        """
        String representation of the MortuaryStaff object.
        """
        return f"Staff {self.staff_id} - {self.position}"
