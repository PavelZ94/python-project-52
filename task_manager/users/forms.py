from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class CreationForm(UserCreationForm):

    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')
