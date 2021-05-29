from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def index(request):
    return render(request, 'base.html')


def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        user = authenticate(username=name, password=password)

        if user is not None:
            login(request)
            return HttpResponse('Вы вошли')
        else:
            return HttpResponse('Нет такого пользователя')
    elif request.method == 'GET':
        return render(request, 'login.html')


def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password_rep = request.POST['password_rep']

        new_user = User.objects.create_user(username=name, email=email, password=password)
        new_user.save()
    elif request.method == 'GET':

        return render(request, 'registration.html')
