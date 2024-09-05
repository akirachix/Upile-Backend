from django.db import models

# Create your models here.
class MortuaryStaff(models.Model):
    staff_id = models.SmallIntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=30)
    contact = models.CharField(max_length=15)
    mortuary_id = models.ForeignKey(Mortuary, on_delete=models.CASCADE)
    generated_code = models.CharField(max_length=30)

    def __str__(self):
        return f"Staff {self.staff_id} - {self.position}"
