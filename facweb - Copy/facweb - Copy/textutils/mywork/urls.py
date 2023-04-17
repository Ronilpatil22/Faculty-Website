from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('mywork/',views.mywork , name='mywork'),
]