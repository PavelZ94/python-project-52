from django import forms
from .models import Task
from django.utils.translation import gettext as _
from task_manager.statuses.models import Status
from task_manager.users.models import User


class TaskForm(forms.ModelForm):

    name = forms.CharField(max_length=100, required=True, label=_('Name'))

    #description = forms.CharField(max_length=150, label=_('Description'))

    status = forms.ModelChoiceField(required=False, label=_('Status'), queryset=Status.objects.all(),)

    executor = forms.ModelChoiceField(
        label=_('Executor'),
        queryset=User.objects.all(),
        required=False,
    )
    class Meta:
        model = Task
        fields = ('name',
                  'description',
                  'status',
                  'executor',
                  )
