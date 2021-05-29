from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


def index(request):
    res = False
    if request.user.is_authenticated:
        res = True
    return render(request, 'base.html', {'auth': res})


def login_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(request, username=name, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return HttpResponse('Нет такого пользователя')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('index')


def registration_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password_rep = request.POST['password_rep']

        new_user = User.objects.create_user(username=name, email=email, password=password)
        new_user.save()

        return redirect('login')
    return render(request, 'registration.html')


def profile_view(request):
    return render(request, 'profile.html')