from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CarType(models.Model):
    model = models.CharField(max_length=30)
    contaminationRate = models.FloatField(default=1)

    def __str__(self):
        return "{} ({})".format(self.model, self.contaminationRate)


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    cardId = models.CharField(max_length=8)
    points = models.IntegerField(default=0)

    carType = models.ForeignKey(CarType, on_delete=models.SET_NULL, null=True)
    passengers = models.IntegerField(default=1)

    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


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
