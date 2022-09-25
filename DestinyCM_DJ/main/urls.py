from django.urls import path

from . import views

app_name = 'main' #define namespace for this project

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('overview/', views.overview, name='overview'),
]