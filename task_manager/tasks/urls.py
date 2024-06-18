from django.urls import path
from .views import (IndexView,
                    CreateView,
                    UpdateView,
                    DeleteView,
                    ShowView)

urlpatterns = [
    path('', IndexView.as_view(), name='tasks'),
    path('create/', CreateView.as_view(), name='task_create'),
    path('<int:pk>/update/', UpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', DeleteView.as_view(), name='task_delete'),
    path('<int:pk>/', ShowView.as_view(), name='task_show'),
]
