from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'index.html'


class Login(LoginView):
    next_page = reverse_lazy('homepage')
    template_name = 'login.html'


class Logout(LogoutView):
    next_page = 'index.html'
