from django.shortcuts import render, redirect, HttpResponse
from django.urls import path, resolve, Resolver404
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate, views as auth_views
from .models import Food, Drink

# Create your views here.

def base_page_viewer(request):
    return render(request, 'login.html', context={})


def home(request):
    return render(request, 'index.html', context={})


def food_viewer(request):
    foods = Food.objects.all() # Извлекаем все продукты из базы данных
    return render(request, 'food.html', context={'foods' : foods})


def drinks_viewer(request):
    drinks = Drink.objects.all()
    return render(request, 'drinks.html', context={'drinks' : drinks})


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

# -------------------------------------------------------------------------

# def url_checker(request):
#     try:
#         # Проверяем, существует ли URL, соответствующий текущему запросу
#         resolve(request.path)
#     except Resolver404:
#         return HttpResponse('Page does not exist')
#     return None


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


def add_food_to_cart(request, food_id):
    food_item = Food.objects.get(id=food_id)
    cart = request.session.get('cart', [])

    cart.append({
        'id': food_item.id,
        'title': food_item.title,
        'price': round(float(food_item.price), 2) # Преобразуем Decimal в float
    })
    request.session['cart'] = cart
    return redirect('food')


def add_drink_to_cart(request, drink_id):
    drink_item = Drink.objects.get(id=drink_id)
    cart = request.session.get('cart', [])
    cart.append({
        'id': drink_item.id,
        'title': drink_item.title,
        'price': round(float(drink_item.price), 2) # Преобразуем Decimal в float
    })
    request.session['cart'] = cart
    return redirect('drinks')


def payment_confirmation_viewer(request):
    if request.method == 'POST':
        cart = request.session.get('cart', [])
        # Получаем данные из корзины (например, из сессии)

        request.session['cart'] = cart
        # Сохраняем их для обработки на странице оплаты

        return render(request, 'payment_confirmation.html', {'cart': cart})
    return HttpResponse('Error with method post')

# --------------------------------------------------------------------------------------------------------
# NOT USED

def checkout(request):
    # Получаем данные из сессии
    cart = request.session.get('checkout_cart', [])
    return render(request, 'checkout.html', {'cart': cart})
# --------------------------------------------------------------------------------------------------------

def cart_viewer(request):
    cart = request.session.get('cart', [])
    # total_price = round(float(sum(item['price'] for item in cart)), 2)
    total_price = round(sum(item['price'] for item in cart), 2)
    return render(request, 'cart.html', {'cart': cart, 'total_price': total_price})


def payment_success_viewer(request):
    return render(request, 'payment_success.html', context={})
