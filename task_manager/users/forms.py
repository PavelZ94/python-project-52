from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class CreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username')
