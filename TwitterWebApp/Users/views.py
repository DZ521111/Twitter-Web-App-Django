'''
Author : Dhruv B Kakadiya

'''
# importing important modules from django

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .all_forms import RegistrationForm

# Create your views here.

# login view which are built in
def login(request):
    return (render(request, "all_users_pages/login.html"))


# for registration purpose here we create register method
