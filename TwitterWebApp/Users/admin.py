'''
Author : Dhruv B Kakadiya

'''
from django.contrib import admin
from .models import User_Profile, Connection

# Register your models here.

admin.site.register(User_Profile)
admin.site.register(Connection)