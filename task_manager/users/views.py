from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from .models import User
from .forms import CreationForm
from task_manager.mixins import RulesMixin, DeleteProtectionMixin
# Create your views here.


class IndexView(ListView):
    """Userlist view"""
    model = User
    template_name = 'users/index.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.all()


class SignUp(SuccessMessageMixin, CreateView):
    """User register view"""
    model = User
    form_class = CreationForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    success_message = _('User is registered successfully')


class Update(RulesMixin, SuccessMessageMixin, UpdateView):
    """User edit view"""
    model = User
    form_class = CreationForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users')
    success_message = _('User settings was updated')


class Delete(DeleteProtectionMixin,
             RulesMixin,
             SuccessMessageMixin,
             DeleteView):
    """User delete view"""
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users')
    success_message = _('User was deleted successfully')
    protected_message = _('''It is not possible to delete this user,
    because it is related to tasks''')
    protected_url = reverse_lazy('users')
