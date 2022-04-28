import re
from django.shortcuts import render

def login(request):
    return render(request, "planttracker/login.html")

def NewUser(request):
    return render(request, "planttracker/NewUser.html")