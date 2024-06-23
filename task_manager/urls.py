"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#from django.views.defaults import server_error, page_not_found
from .views import (IndexView,
                    UserLogin,
                    Logout)

urlpatterns = [
    path('', IndexView.as_view(), name='homepage'),
    path('admin/', admin.site.urls),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('users/', include('task_manager.users.urls')),
    path('statuses/', include('task_manager.statuses.urls')),
    path('tasks/', include('task_manager.tasks.urls')),
    path('labels/', include('task_manager.labels.urls')),
]

handler404 = "task_manager.views.page_not_found_view"
#handler404 = curry(page_not_found, exception=Exception('Page not Found'), template_name='404.html')
#handler500 = curry(server_error, exception=Exception('Server Error'), template_name='500.html')
