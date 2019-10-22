from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    carType = models.CharField(max_length=30, blank=True)


class Viajes(models.Model):
    start = models.CharField(max_length=8)
    end = models.CharField(max_length=8)
    points = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
