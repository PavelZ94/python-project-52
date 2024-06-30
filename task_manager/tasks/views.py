from django.views.generic import (CreateView,
                                  UpdateView,
                                  DeleteView,
                                  DetailView)
from django_filters.views import FilterView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from .models import Task
from .forms import TaskForm
from .filters import TaskFilter
from task_manager.mixins import TaskDeleteProtection
# Create your views here.


class IndexView(LoginRequiredMixin, FilterView):
    """Tasklist view"""
    model = Task
    template_name = 'tasks/index.html'
    filterset_class = TaskFilter
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.all()


class CreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """Task create view"""
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task was created successfully')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ShowView(DetailView):
    """View of  determined task"""
    model = Task
    template_name = 'tasks/show.html'


class UpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Task edit view"""
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task was updated successfully')
    login_url = reverse_lazy('login')


class DeleteView(LoginRequiredMixin,
                 TaskDeleteProtection,
                 SuccessMessageMixin,
                 DeleteView):
    """Task delete view"""
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task was deleted successfully')
    author_message = _('The task can be deleted only by its author')
    author_url = reverse_lazy('tasks')
    login_url = reverse_lazy('login')
