from django.urls import path
from .views import (IndexView,
                    CreateView,
                    UpdateView,
                    DeleteView)


urlpatterns = [
    path('', IndexView.as_view(), name='labels'),
    path('create/', CreateView.as_view(), name='label_create'),
    path('<int:pk>/update/', UpdateView.as_view(), name='label_update'),
    path('<int:pk>/delete/', DeleteView.as_view(), name='label_delete'),
]
