from django.shortcuts import render

# Create your views here.

def index(response):
    return render(response, 'main/base.html', {})

def overview(response):
    return render(response, 'main/login.html', {})