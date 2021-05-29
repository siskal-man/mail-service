from django.urls import path

from .views import index, login_view, registration, logout_view

urlpatterns = [
    path('', index, name='index'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('registration', registration, name='registration'),
]
