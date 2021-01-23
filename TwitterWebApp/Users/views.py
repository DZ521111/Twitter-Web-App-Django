'''
Author : Dhruv B Kakadiya

'''
# importing important modules from django

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .all_forms import RegistrationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# login view which are built in



# for registration purpose here we create register method
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})