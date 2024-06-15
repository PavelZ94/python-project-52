from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.

class IndexView(ListView):
    model = Status
    template_name = 'statuses/index.html'
    context_object_name = 'statuses'

    def get_queryset(self):
        return Status.objects.all()
