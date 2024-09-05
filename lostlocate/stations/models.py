from django.db import models

# Create your models here.
class PoliceStation(models.Model):
    station_id = models.SmallIntegerField(primary_key=True)
    station_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.station_name