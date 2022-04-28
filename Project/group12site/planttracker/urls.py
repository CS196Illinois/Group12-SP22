import imp
from unicodedata import name
from django.urls import path
from planttracker import views as plantviews

urlpatterns = [
    path('', plantviews.login, name="login"),
    path('login/', plantviews.login, name="login"),
    path('NewUser/', plantviews.NewUser, name="NewUser"),
]