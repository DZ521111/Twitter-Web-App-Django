from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Tweets, Comment, Preference
from django.db.models import Count
from django.contrib.auth.models import User, Group
import sys
from Users import Connection, User_Profile

# Create your views here.

# static variables
page_count = 3

'''def home_tweet(request):
    return (render(request, 'all_tweet_pages/home_tweet.html'))
'''

# check whether there is user or not! hwo are tweeting.
def is_users(tweet_user, logged_user):
    return (tweet_user == logged_user)



# class for viewing all tweet views
class AllTweetView(LoginRequiredMixin, ListView):
    model = Tweets
    template_name = 'home_tweet.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = page_count

    # get context data as a dictionary
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        all_users = []
        data_counter = Tweets.objects.values('author')\
            .annotate(author_count = Count('author'))\
            .order_by('-author_count')[:6]

        for aux in data_counter:
            all_users.append(User.objects.filter(pk=aux['author']).first())

        data['preference'] = Preference.objects.all()
        data['all_users'] = all_users
        print(all_users, file = sys.stderr)
        return data

    # to fetch query set
    def get_queryset(self):
        user = self.request.user
        qs = Connection.objects.filter(user = user)
        follows = [user]
        for obj in qs:
            follows.append(obj.follow_user)
        return Tweets.objects.filter(author__in = follows).order_by('-date_posted')

# about us page function
def aboutus(request):
    return (render(request, 'aboutus.html'))