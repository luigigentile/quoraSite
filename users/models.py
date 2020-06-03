from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    luogodinascita =  models.CharField(max_length=240,null=True)
    pass
