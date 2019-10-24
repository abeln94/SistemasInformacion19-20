from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CarTypes(models.Model):
    display = models.CharField(max_length=8)


class User(AbstractUser):
    carType = models.ForeignKey(CarTypes, on_delete=models.SET_NULL, null=True)
    points = models.IntegerField(default=0)


class Viajes(models.Model):
    start = models.CharField(max_length=8)
    end = models.CharField(max_length=8)
    points = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
