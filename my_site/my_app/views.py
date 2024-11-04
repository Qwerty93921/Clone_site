from django.shortcuts import render, redirect, HttpResponse
from http.client import responses
from wsgiref.util import request_uri
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.urls import resolve, Resolver404

# Create your views here.

def base_page_viewer(request):
    return render(request, 'index.html', context={})


def home(request):
    return render(request, 'index.html', context={})


def food_viewer(request):
    return render(request, 'food.html', context={})


def drinks_viewer(request):
    return render(request, 'drinks.html', context={})


def about_viewer(request):
    return render(request, 'about.html', context={})


# def login_page_viewer(request):
#     return render(request, 'login.html', context={})


# def logout_viewer(request):
#     return render(request, 'logout.html', {'user' : User})


def logout_viewer(request):
    logout(request)
    return redirect('login') # Выход на эту страницу после logout

# -------------------------------------------------------------------------

# def register_page_viewer(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#     return render(request, 'register.html', {'form' : form})

# -------------------------------------------------------------------------

# def register_page_viewer(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             # Сохранение данных в модели, например:
#             user = form.save()
#             return redirect('home')  # Перенаправляем на другую страницу после успешной регистрации
#     else:
#         form = RegisterForm()  # Если это GET-запрос, создаём пустую форму
#
#     return render(request, 'register.html', {'form': form})

def register_page_viewer(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print("Форма валидна и данные сохраняются")
            user = form.save()  # Сохраняем нового пользователя
            login(request, user)  # Вход после регистрации
            user.save()
            # user.set_password(form.cleaned_data['password'])  # Храните пароль в зашифрованном виде
            # user.password = make_password(form.cleaned_data['password'])

            # Аутентифицируем пользователя по имени и паролю
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            # Выполняем вход, если аутентификация успешна
            if user is not None:
                login(request, user)
                print("Пользователь успешно аутентифицирован и залогинен.")
                return redirect('home')  # Замените 'home' на страницу, куда хотите перенаправить пользователя после регистрации
        else:
            print("Форма не валидна. Ошибки:", form.errors)
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


# def url_checker(request):
#     try:
#         # Проверяем, существует ли URL, соответствующий текущему запросу
#         resolve(request.path)
#     except Resolver404:
#         return HttpResponse('Page does not exist')
#     return None
