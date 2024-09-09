from django.db import models
# from users.models import User
from stations.models import PoliceStation

# Create your models here.


class PoliceOfficer(models.Model):
    """Primary key for the PoliceOfficer model"""
    officer_id = models.SmallIntegerField(primary_key=True)
    
    # ForeignKey linking PoliceOfficer to a User (currently commented out)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    """Officer's rank (e.g., Sergeant, Inspector, etc.)"""
    rank = models.CharField(max_length=30)

    """Contact number of the officer"""
    contact = models.CharField(max_length=15)

    """ForeignKey linking PoliceOfficer to a PoliceStation"""
    station_id = models.ForeignKey(PoliceStation, on_delete=models.CASCADE)

    """ A generated code, possibly for internal tracking or verification"""
    generated_code = models.CharField(max_length=30)

    def __str__(self):
        """String representation of the object for display purposes"""
        return f"Officer {self.officer_id} - {self.rank}"