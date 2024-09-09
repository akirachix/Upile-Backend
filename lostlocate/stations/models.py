from django.db import models

# Create your models here.
class PoliceStation(models.Model):
    # Primary key for the PoliceStation model
    station_id = models.SmallIntegerField(primary_key=True)

    # Name of the police station
    station_name = models.CharField(max_length=50)

    # Location of the police station (could be a city, district, etc.)
    location = models.CharField(max_length=50)

    def __str__(self):
        # String representation of the object for display purposes
        return self.station_name
