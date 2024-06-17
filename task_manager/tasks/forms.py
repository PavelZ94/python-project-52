from django import forms
from .models import Task
from django.utils.translation import gettext as _


class TaskForm(forms.ModelForm):

    name = forms.CharField(max_length=100, required=True, label=_('Name'))

    description = forms.CharField(max_length=150, label=_('Description'))

    class Meta:
        model = Task
        fields=('name',
                'description',
                'status',
                'executor',
                )