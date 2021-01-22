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
        # call super class get_context_data method to get data
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

class UserTweetView(LoginRequiredMixin, ListView):
    model = Tweets
    template_name = 'user_posts.html'
    context_object_name = 'posts'
    paginate_by = page_count

    def visible_user(self):
        return (get_object_or_error(User, username = self.kwargs.get('username')))

    def get_context_data(self, **kwargs):
        visible_user = self.visible_user()
        logged_user = self.request.user
        print(logged_user.username == '', file = sys.stderr)

        if ((logged_user.username == '') or (logged_user is None)):
            can_follow = False
        else:
            can_follow = (Connection.objects.filter(user = logged_user, follow_user = visible_user).count() == 0)

        data = super().get_context_data(**kwargs)
        data['user_profile'] = visible_user
        data['can_follow'] = can_follow
        return (data)

    def get_queryset(self):
        user = self.visible_user()
        return Tweets.objects.filter(author = user).order_by('-date_posted')

    def post(self, request, *args, **kwargs):
        if request.user.id is not None:
            follows_between = Connection.objects.filter(user = request.user, follow_user = self.visible_user())

            if ('follow' in request.POST):
                    new_relation = Connection(user = request.user, follow_user = self.visible_user())
                    if (follows_between.count() == 0):
                        new_relation.save()
            elif ('unfollow' in request.POST):
                    if (follows_between.count() > 0):
                        follows_between.delete()

        return (self.get(self, request, *args, **kwargs))