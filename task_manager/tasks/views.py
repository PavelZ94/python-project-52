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
# Create your views here.


class IndexView(LoginRequiredMixin, FilterView):
    model = Task
    template_name = 'tasks/index.html'
    filterset_class = TaskFilter
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.all()


class CreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
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
    model = Task
    template_name = 'tasks/show.html'


class UpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task was updated successfully')
    login_url = reverse_lazy('login')


class DeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks')
    success_message = _('Task was deleted successfully')
    login_url = reverse_lazy('login')
