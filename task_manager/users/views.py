from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.
from .models import User
from .forms import CreationForm

class IndexView(ListView): #Check, what is it
    model = User
    template_name = 'users/index.html'


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('templates/index.html')
    template_name = 'templates/users/create.html'
