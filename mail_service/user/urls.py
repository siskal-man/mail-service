from django.urls import path

from .views import index, login_view, registration_view, logout_view, profile_view

urlpatterns = [
    path('', index, name='index'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('registration', registration_view, name='registration'),
    path('profile', profile_view, name='profile'),
]
