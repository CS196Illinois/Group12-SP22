import imp
from unicodedata import name
from django.urls import path
from planttracker import views as plantviews

urlpatterns = [
    path('', plantviews.index, name="Home"),
    path('NewUser/', plantviews.NewUser, name="NewUser"),
]