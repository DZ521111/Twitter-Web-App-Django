'''
Author : Dhruv B Kakadiya

'''
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Tweets

# user serializers
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

# group serializers
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

# tweet serializers
class TweetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweets
        fields = ['content', 'author']