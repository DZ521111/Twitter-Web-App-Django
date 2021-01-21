from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

# Create your views here.

'''def home_tweet(request):
    return (render(request, 'all_tweet_pages/home_tweet.html'))
'''

# class for viewing all tweet views
class AllTweetView(LoginRequiredMixin, ListView):
    template_name = "home_tweet.html"
    def get_queryset(self):
        pass

# about us page function
def aboutus(request):
    return (render(request, 'aboutus.html'))