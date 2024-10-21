from django.db import models

class Plant(models.Model):
    trefle_id = models.IntegerField(unique=True)
    common_name = models.CharField(max_length=255)
    scientific_name = models.CharField(max_length=255)
    family = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    

    def __str__(self):
        return self.common_name or self.scientific_name