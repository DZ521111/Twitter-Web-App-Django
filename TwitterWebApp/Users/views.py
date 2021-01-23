'''
Author : Dhruv B Kakadiya

'''
# importing important modules from django

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .all_forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from .all_forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User

# Create your views here.

# login view which are built in
'''def login(request):
    pass
'''


# for registration purpose here we create register method
def register(request):
    if (request.method == "POST"):
        form = RegistrationForm(request.POST)
        if (form.is_valid()):
            form.save()
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            messages.success(request, f'Account created for {username}! and email {email}')
            return (redirect('login'))
    else:
        form = RegistrationForm()
    return (render(request, 'register.html', {'form': form}))



@login_required
def profile(request):
    if (request.method == "POST"):
        usform = UserUpdateForm(request.POST, instance = request.user)
        prform = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)

        if ((usform.is_valid()) and (prform.is_valid())):
            usform.save()
            prform.save()
            messages.success(request, f'Account has been updated.')
            return (redirect("profile"))
    else:
        usform = UserUpdateForm(instance = request.user)
        prform = ProfileUpdateForm(instance = request.user.profile)

    return (render(request, 'users/profile.html', {'usform': usform, 'prform': prform}))



@login_required
def SearchResult(request):
    if (request.method == "POST"):
        result = request.POST.get('search')
        #print(kerko)
        results = User.objects.filter(username__contains = result)
        context = { 'results': results }
        return render(request, 'search_user.html', context)