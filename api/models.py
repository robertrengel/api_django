from django.db import models


class Programmer(models.Model):
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)


# Create your models here.
