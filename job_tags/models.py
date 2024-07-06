from django.db import models


class JobTag(models.Model):
    id = models.AutoField(primary_key=True)  # افزودن id به عنوان کلید اصلی
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
