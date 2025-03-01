from django.db import models
from django.contrib.auth.models import AbstractUser
from myapp.manager import UserManager
# Create your models here.
class CustomeUser(AbstractUser):
    username=None
    phone_number=models.CharField(max_length=50,unique=True)
    user_info = models.CharField(max_length=100)

    USERNAME_FIELD='phone_number'
    objects=UserManager()