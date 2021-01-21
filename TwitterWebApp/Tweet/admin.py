'''
Author : Dhruv B Kakadiya

'''
# import importance libraries
from django.contrib import admin
from .models import Tweets, Comment, Preference

# Register your models here.
admin.site.register(Tweets)
admin.site.register(Comment)
admin.site.register(Preference)