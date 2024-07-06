from django.db import models

# Create your models here.

from django.db import models


class Location(models.Model):
    id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=255)

    def __str__(self):
        return self.city_name
