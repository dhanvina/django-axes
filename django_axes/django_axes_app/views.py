from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse("You're logged in!")
        else:
            return HttpResponse("Login failed!")
    return render(request, 'django_axes_app/login.html')

def lockout_view(request, *args, **kwargs):
    return render(request, 'django_axes_app/lockout.html', {})
