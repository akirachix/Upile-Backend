from django.core.exceptions import ValidationError
from django.db import models

class PoliceStation(models.Model):
    """Defines a PoliceStation model with an ID, name, and location."""
    id = models.AutoField(primary_key=True)  # Use AutoField for automatic ID generation
    station_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.station_name

    def clean(self):
        # Custom validation logic
        if not self.station_name or not self.location:
            raise ValidationError("Both station_name and location are required.")

    def save(self, *args, **kwargs):
        self.clean()  # Apply custom validation
        super().save(*args, **kwargs)
