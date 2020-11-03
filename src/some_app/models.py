from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager

# Create your models here.
class User(AbstractBaseUser):
  email = models.EmailField(max_length=255)
  username = models.CharField(max_length=255, unique=True)
  hair_color = models.CharField(max_length=255)

  objects = UserManager()
  
  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = []

  def __str__(self):
    return self.username