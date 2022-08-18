from django.urls import re_path as url
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index')
]
