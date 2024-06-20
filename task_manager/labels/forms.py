from django import forms
from .models import Label
from django.utils.translation import gettext as _


class LabelForm(forms.ModelForm):

    name = forms.CharField(required=True, label=_('Name'))

    class Meta:
        model = Label
        fields = ('name',)
