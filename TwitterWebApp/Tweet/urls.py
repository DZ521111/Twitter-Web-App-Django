'''
Author : Dhruv B Kakadiya

'''

from django.urls import path, include
from .views import ( AllTweetView)

urlpatterns = [
     path('',  AllTweetView.as_view(), name='home_tweet_page'),
     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]