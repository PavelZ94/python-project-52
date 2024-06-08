from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
# Create your views here.
from .models import User
from .forms import CreationForm


class IndexView(ListView):
    template_name = 'users/index.html'


class SignUp(SuccessMessageMixin, CreateView):
    model = User
    form_class = CreationForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    success_message = 'User is registered successfully'


class Update(SuccessMessageMixin, UpdateView):
    model = User
    form_class = CreationForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users')
    success_message = 'User settings was updated'

class Delete(SuccessMessageMixin, DeleteView):
    model = User
    form_class = CreationForm
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users')
    success_message = 'User was deleted successfully'
