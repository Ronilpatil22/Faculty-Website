from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('creators/',views.creators , name='creators'),
]
