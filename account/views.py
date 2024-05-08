from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def logout(request):
    return render(request, 'home/home.html')

def signup(request):
    return render(request, 'account/signup.html')

def signup_done(request):
    pass