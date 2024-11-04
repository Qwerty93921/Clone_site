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
from django.contrib.auth.views import LogoutView
from .views import (home, base_page_viewer, food_viewer, drinks_viewer, register_page_viewer,
                    auth_views,
                    about_viewer, logout_viewer)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_page_viewer, name='index'),
    path('home/', home, name='home'),
    path('food/', food_viewer, name='food'),
    path('drinks/', drinks_viewer, name='drinks'),
    path('about/', about_viewer, name='about'),
    # path('login/', login_page_viewer, name='login'),
    path('register/', register_page_viewer, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('logout/', logout_viewer, name='logout'),
    # path('my_profile/', user_profile_viewer, name='profile_viewer'),
]
