from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _


class CreationForm(UserCreationForm):

    first_name = forms.CharField(max_length=150, required=True, label=_('First name'))
    last_name = forms.CharField(max_length=150, required=True, label=_('Last name'))

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')

    def clean_username(self):
        return self.cleaned_data.get('username')
