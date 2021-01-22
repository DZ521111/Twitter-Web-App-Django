'''
Author : Dhruv B Kakadiya

'''

# import some important library for forms
from django import forms
from .models import Comment

# form for new comment
class NewComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
