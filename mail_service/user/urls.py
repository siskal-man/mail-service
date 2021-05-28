from django.contrib import admin
from django.urls import path

from .views import index, login, registration

urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login'),
    path('registration', registration, name='registration'),
]
