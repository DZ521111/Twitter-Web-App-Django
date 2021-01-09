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
    profile_pic = models.ImageField(default = "default_profile_pic.png", upload_to = "profile_images")
    def __str__(self):
        return (f"{self.user.username} Profile")

    # number of following of perticular user
    @property
    def followings(self):
        return (Connection.objects.filter(user = self.user).count())

    # number of following of perticular user
    @property
    def followers(self):
        return (Connection.objects.filter(follow_users = self.user).count())

    # to save the perticular user
    def save(self, force_insert=False, force_update = False, using=None, update_fields=None):
        # call the save function of super (Model) class
        super().save()

        # to save the profile pic
        img = Image.open(self.profile_pic.path)
        if ((img.height > 300) or (img.width > 300)):
            pic_size = (280, 280)
            img.thumbnail(pic_size)
            img.save(self.profile_pic.path)


# connection class Model
class Connection (models.Model):
    user = models.ForeignKey(User, related_name = 'user', on_delete = models.CASCADE)
    follow_users = models.ForeignKey(User, related_name = 'follow_users', on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)