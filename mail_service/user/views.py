from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
# from django.contrib.auth.hashers import make_password


def check_att(cur_att, new_att):
    if new_att:
        return new_att
    return cur_att


def index(request):
    if request.user.is_authenticated:
        res = False
        if request.user.is_authenticated:
            res = True
        return render(request, 'base.html', {'auth': res})
    else:
        return redirect('login')


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
    if request.user.is_authenticated:
        logout(request)
        return redirect('index')
    else:
        return redirect('login')


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
    if request.user.is_authenticated:
        cur_user = request.user
        return render(request, 'profile.html', {'user': cur_user})
    else:
        return redirect('login')


# def profile_settings_view(request):
#     if request.user.is_authenticated:
#         cur_user = User.objects.get(username=request.user.username)
#         if request.method == 'POST':
#             new_username = request.POST.get('name')
#             new_email = request.POST.get('new_email')
#             new_password = request.POST.get('password')
#
#             cur_user.username = check_att(cur_att=cur_user.username, new_att=new_username)
#             cur_user.email = check_att(cur_att=cur_user.email, new_att=new_email)
#
#             cur_user.password = make_password(new_password)
#             cur_user.save()
#
#             cur_user = User.objects.get(username=request.user.username)
#             user = authenticate(request, username=cur_user.username, password=cur_user.password)
#
#             login(request, user)
#             return redirect('settings')
#
#         return render(request, 'settings.html', {'user': cur_user})
#     else:
#         return redirect('login')


def user_contacts_view(request):
    if request.user.is_authenticated:
        return render(request, 'contacts.html')
    else:
        return redirect('login')
