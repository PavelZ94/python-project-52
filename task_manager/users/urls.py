from django.urls import path
from .views import (IndexView,
                    SignUp,
                    Update,
                    Delete)


urlpatterns = [
    path('', IndexView.as_view(), name='users'),
    path('create/', SignUp.as_view(), name='user_create'),
    path('<int:pk>/update/', Update.as_view(), name='user_update'),
    path('<int:pk>/delete/', Delete.as_view(), name='user_delete'),
]
