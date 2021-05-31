from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def check_att(cur_att, new_att):
    if new_att:
        return new_att
    return cur_att


@login_required
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


@login_required
def profile_view(request):
    cur_user = request.user
    return render(request, 'profile.html', {'user': cur_user})


@login_required
def profile_settings_view(request):
    cur_user = request.user
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        cur_user.username = check_att(cur_att=cur_user.username, new_att=username)

    return render(request, 'settings.html', {'user': cur_user})


@login_required
def user_contacts_view(request):
    return render(request, 'contacts.html')
