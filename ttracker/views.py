# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .models import *


def home(request):
    return render(request, 'pages/home.html')


def login(request):
    return render(request, 'pages/login.html')
