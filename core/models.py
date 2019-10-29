from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CarType(models.Model):
    model = models.CharField(max_length=30)
    contaminationRate = models.FloatField(default=1)


class User(AbstractUser):
    cardId = models.CharField(max_length=8)
    points = models.IntegerField(default=0)

    carType = models.ForeignKey(CarType, on_delete=models.SET_NULL, null=True)
    passengers = models.IntegerField(default=1)


class Trip(models.Model):
    date = models.DateTimeField()
    start = models.CharField(max_length=50)
    end = models.CharField(max_length=50)
    points = models.IntegerField(default=0)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
