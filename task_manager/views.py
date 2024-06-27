from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from django.urls import reverse_lazy


class IndexView(TemplateView):
    """Homepage view"""
    template_name = 'index.html'


class UserLogin(SuccessMessageMixin, LoginView):
    """Authenticate user view"""
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('homepage')
    success_message = _('You are logged in successfully')

    def form_valid(self, form):
        return super().form_valid(form)


class Logout(LogoutView):
    """Logout user view"""

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)


def tk_handler_404(request, exception):
    """Render 404 error page if requested page is missing."""
    return render(request=request, template_name='404.html', status=404)


def tk_handler_500(request):
    """Render 500 error if unable to connect server."""
    return render(request=request, template_name='500.html', status=500)
