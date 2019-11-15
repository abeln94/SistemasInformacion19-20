from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CarType(models.Model):
    model = models.CharField(max_length=30)
    contaminationRate = models.FloatField(default=1)

    def __str__(self):
        return "{} ({})".format(self.model, self.contaminationRate)


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


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    imageAlt = models.CharField(max_length=200)
    content = models.TextField()

    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title