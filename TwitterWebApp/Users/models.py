'''
Author : Dhruv B Kakadiya

'''

from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.

# Class Model for User Profile
class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default = "default_profile_pic.png", upload_to = "profile_images")
