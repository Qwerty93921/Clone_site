"""
URL configuration for my_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path, include
from .views import home, base_page_viewer, books_list_viewer, cars_viewer, login_page_viewer, register_page_viewer, auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_page_viewer, name='index'),
    path('home/', home, name='home'),
    path('books/', books_list_viewer, name='books'),
    path('cars/', cars_viewer, name='cars'),
    # path('login/', login_page_viewer, name='login'),
    path('register/', register_page_viewer, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]
