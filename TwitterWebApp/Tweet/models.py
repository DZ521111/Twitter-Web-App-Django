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
    likes = models.IntegerField(default = 0)
    dislikes = models.IntegerField(default = 0)
    reports = models.IntegerField(default = 0)

    def __str__(self):
        return self.content[ : 10]

    @property
    def number_of_comments(self):
        return Comment.objects.filter(tweet_connected = self).count()


# class model for Comments
class Comment (models.Model):
    content = models.TextField(max_length = 500)
    date_posted = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    tweet_connected = models.ForeignKey(Tweets, on_delete = models.CASCADE)


# class model for records like dislike and authors
class Preference (models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    tweet = models.ForeignKey(Tweets, on_delete = models.CASCADE)
    value = models.IntegerField()
    date = models.DateTimeField(auto_now = True)

    def __str__(self):
        return (f"{str(self.user)} : {str(self.post)} : {str(self.value)}")

    class Meta:
        unique_together = ("user", "tweet", "value")


