from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.urls import reverse_lazy


class IndexView(TemplateView):
    template_name = 'index.html'


class UserLogin(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('homepage')
    success_message = _('You are logged in successfully')

    def form_valid(self, form):
        return super().form_valid(form)


class Logout(SuccessMessageMixin, LogoutView):
    next_page = reverse_lazy('homepage')

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)
