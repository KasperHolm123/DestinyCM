from django.urls import path
from .views import index_view, overview_view, login_view

app_name = 'main' #define namespace for this project

urlpatterns = [
    path('', index_view.index, name='index'),
    path('login/', login_view.login, name='login'),
    path('overview/', overview_view.overview, name='overview'),
]