from django.contrib import admin
from django.urls import path
from project import views

urlpatterns = [
    path('', views.index),
    path('first/', views.first),
    path('second/', views.second),
]
