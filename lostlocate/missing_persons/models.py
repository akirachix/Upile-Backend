from django.db import models
# from police.models import PoliceOfficer
# Create your models here.
class MissingPerson(models.Model):
    missing_person_id = models.SmallIntegerField(primary_key=True)
    # officer_id = models.ForeignKey(PoliceOfficer, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    age = models.SmallIntegerField()
    gender = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    image = models.ImageField(upload_to='missing_persons/')
    height = models.FloatField()
    weight = models.FloatField()
    hair_color = models.CharField(max_length=50)
    eye_color = models.CharField(max_length=50)
    skin_color = models.CharField(max_length=50)
    missing_date = models.DateTimeField()
    location = models.CharField(max_length=50)
    clothes_worn = models.TextField()
    def __str__(self):
        return f"{self.name}"