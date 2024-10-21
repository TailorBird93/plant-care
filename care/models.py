from django.db import models
from django.contrib.auth.models import User
from plants.models import Plant

class CareTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    task = models.CharField(max_length=255)
    frequency = models.CharField(max_length=100)  # e.g., Daily, Weekly
    next_due = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.task} for {self.plant.common_name}"

