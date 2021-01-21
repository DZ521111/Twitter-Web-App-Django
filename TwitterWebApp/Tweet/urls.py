'''
Author : Dhruv B Kakadiya

'''

from django.urls import path, include
from .views import ( AllTweetView )
from . import views

urlpatterns = [
     path('',  AllTweetView.as_view(), name='home_tweet_page'),
     path('about/', views.aboutus, name='tweet_aboutus'),
     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]