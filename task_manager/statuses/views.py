from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import Status
from .forms import StatusForm
from task_manager.mixin import DeleteProtectionMixin
# Create your views here.


class IndexView(ListView):
    """Status list view"""
    model = Status
    template_name = 'statuses/index.html'
    context_object_name = 'statuses'

    def get_queryset(self):
        return Status.objects.all()


class CreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Status create view"""
    model = Status
    form_class = StatusForm
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses')
    success_message = _('Status was created successfully')
    login_url = reverse_lazy('login')


class UpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Status edit view"""
    model = Status
    form_class = StatusForm
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses')
    success_message = _('Status was updated successfully')
    login_url = reverse_lazy('login')


class DeleteView(DeleteProtectionMixin,
                 LoginRequiredMixin,
                 SuccessMessageMixin,
                 DeleteView):
    """Status delete view"""
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses')
    success_message = _('Status was deleted successfully')
    login_url = reverse_lazy('login')
    protected_message = _('''It is not possible to delete this status,
    because it is related to tasks''')
    protected_url = reverse_lazy('statuses')
