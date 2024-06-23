from django import forms
from .models import Task
from django.utils.translation import gettext as _
from task_manager.statuses.models import Status
from task_manager.users.models import User
from task_manager.labels.models import Label


class TaskForm(forms.ModelForm):

    name = forms.CharField(required=True,
                           label=_('Name'))

    description = forms.CharField(label=_('Description'),
                                  required=False)

    status = forms.ModelChoiceField(required=False,
                                    label=_('Status'),
                                    queryset=Status.objects.all(),)

    executor = forms.ModelChoiceField(label=_('Executor'),
                                      queryset=User.objects.all(),
                                      required=False,)

    label = forms.ModelMultipleChoiceField(queryset=Label.objects.all(),
                                           label=_('Label'),
                                           required=False)

    class Meta:
        model = Task
        fields = ('name',
                  'description',
                  'status',
                  'executor',
                  'label',
                  )
