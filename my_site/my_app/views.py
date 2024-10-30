from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import RegisterForm
from django.contrib.auth import login, authenticate

# Create your views here.

def base_page_viewer(request):
    return render(request, 'index.html', context={})


def home(request):
    return render(request, 'index.html', context={})


def books_list_viewer(request):
    return render(request, 'books.html', context={})


def cars_viewer(request):
    return render(request, 'cars.html', context={})


def about_viewer(request):
    return render(request, 'about.html', context={})


def login_page_viewer(request):
    return render(request, 'login.html', context={})


def logout_viewer(request):
    return render(request, 'logout.html', {'user' : User})


def user_profile_viewer(request):
    return render(request, 'user_profile.html', {'user': User})
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
