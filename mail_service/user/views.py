from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse

def index(request):
    return render(request, 'base.html')


def login(request):
    return render(request, 'login.html')


def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password_rep = request.POST['password_rep']

        new_user = User.objects.create_user(username=name, email=email, password=password)
        new_user.save()
        res = [email, password]
    return render(request, 'registration.html')
