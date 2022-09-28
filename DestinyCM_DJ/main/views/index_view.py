from django.shortcuts import render, redirect



def index(response):
    return render(response, 'main/base.html', {})