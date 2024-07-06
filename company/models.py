from django.db import models
from location.models import Location


# Create your models here.

class CompanyCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name_fa = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    category = models.ForeignKey(CompanyCategory, on_delete=models.CASCADE)
    size = models.CharField(max_length=50)
    website = models.URLField()
    established_year = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_en
