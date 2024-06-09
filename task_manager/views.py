from django.views.generic import TemplateView, FormView
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'index.html'


#class Login(SuccessMessageMixin, LoginView):
#    form_class = AuthenticationForm
#    template_name = 'login.html'
#    next_page = reverse_lazy('homepage')
#    success_message = 'You are logged in successfully'
class LoginView(SuccessMessageMixin, FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('homepage')
    success_message = 'You are logged in successfully'

    def form_valid(self, form):
        return super().form_valid(form)


class Logout(SuccessMessageMixin, LogoutView):
    next_page = reverse_lazy('homepage')
    success_message = 'You are logged out'
