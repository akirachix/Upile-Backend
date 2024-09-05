from django.db import models
from users.models import User
from stations.models import PoliceStation

# Create your models here.
class PoliceOfficer(models.Model):
    officer_id = models.SmallIntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rank = models.CharField(max_length=30)
    contact = models.CharField(max_length=15)
    station_id = models.ForeignKey(PoliceStation, on_delete=models.CASCADE)
    generated_code = models.CharField(max_length=30)

    def __str__(self):
        return f"Officer {self.officer_id} - {self.rank}"