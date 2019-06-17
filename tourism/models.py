from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class attractions(models.Model):
    name=models.CharField(max_length=100)
    image=models.CharField(max_length=200)
    img = ArrayField(models.CharField(max_length=1000, blank=True))
    description = ArrayField(models.CharField(max_length=10000, blank=True))
    latitude = models.FloatField(default=27.489595)
    longitude = models.FloatField(default=83.277083)

    def __str__(self):
        return self.name
    
