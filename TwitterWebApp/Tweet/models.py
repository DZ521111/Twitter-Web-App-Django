'''
Author : Dhruv B Kakadiya

'''
# imports important libraries
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# tweets models

class Tweets (models.Model):
    content = models.TextField(max_length = 5000)
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    likes= models.IntegerField(default = 0)
    dislikes= models.IntegerField(default = 0)

    def __str__(self):
        return self.content[ : 10]
