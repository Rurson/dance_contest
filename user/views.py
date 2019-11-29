from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView


class UserView(UserCreationForm):
    # model = User
    # template_name = 'user/signup.html'
    # fields = ['username','password']
    # fields = '__all__'
