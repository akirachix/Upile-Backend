from django.db import models

# Create your models here.
class Mortuary(models.Model):
    mortuary_id = models.SmallIntegerField(primary_key=True)
    mortuary_name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.mortuary_name