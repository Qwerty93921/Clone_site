from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import RegisterForm

# Create your views here.

def base_page_viewer(request):
    return render(request, 'index.html', context={})


def home(request):
    return render(request, 'index.html', context={})


def books_list_viewer(request):
    return render(request, 'books.html', context={})


def cars_viewer(request):
    return render(request, 'cars.html', context={})


def login_page_viewer(request):
    return render(request, 'login.html', context={})


# def register_page_viewer(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.POST)
#     return render(request, 'register.html', {'form' : form})

def register_page_viewer(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Сохранение данных в модели, например:
            user = form.save()
            return redirect('home')  # Перенаправляем на другую страницу после успешной регистрации
    else:
        form = RegisterForm()  # Если это GET-запрос, создаём пустую форму

    return render(request, 'register.html', {'form': form})
