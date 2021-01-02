'''
Author : Dhruv B Kakadiya

'''
# importing important modules from django

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return (render(request, "all_users_pages/login.html"))