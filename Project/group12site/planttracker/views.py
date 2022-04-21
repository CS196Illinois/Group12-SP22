from django.shortcuts import render

# Requests user dashboard
def dashboard(request):
    return render(request, "users/dashboard.html")