from django.shortcuts import render

# Create your views here.

def index(response):
    return render(response, 'main/base.html', {})

def login(response):
    return render(response, 'main/authentication/login.html', {})

def overview(response):
    return render(response, 'main/home/overview.html', {})