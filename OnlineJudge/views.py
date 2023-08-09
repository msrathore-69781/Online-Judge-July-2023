from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login

def home(request):
    return render(request,'home.html')