from main.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def register_user(request):
    if request.method == 'POST':
        User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password']
        )
    return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
    return render(request, 'login.html')


def log_out(request):
    logout(request)
    return redirect('index')
    
"""

from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            User.objects.create_user(username=username, password=password)
        except IntegrityError:
            messages.error(request, "Ushbu foydalanuvchi allaqachon yaratilgan")
            return render(request, 'register.html')
        else:
            messages.success(request, "Yangi foydalanuvchi yaratildi")
            return redirect('index') 
    return render(request, 'register.html')
    
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect('index')  # Assuming 'index' is the name of your URL pattern
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')
"""  

