from django.urls import path
from .views import IndexView, SignUp


urlpatterns = [
    path('', IndexView.as_view(), name='users'),
    path('create/', SignUp.as_view(), name='user_create'),
    path('<int:id>/update/', views.update, name='user_update'),
    path('<int:id>/delete/', views.delete, name='user_delete'),
]
