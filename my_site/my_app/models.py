from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class Food(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    # img =
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(null=False, blank=False, max_digits=10, decimal_places=2)
    amount = models.DecimalField(null=False, blank=False, max_digits=20, decimal_places=0)
    # decimal_places = 2 - значит 2 цифры после запятой, ВСЕГО 10 цифр

    def __str__(self):
        return self.title


class Drink(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    # img =
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(null=False, blank=False, max_digits=10, decimal_places=2)
    amount = models.DecimalField(null=False, blank=False, max_digits=20, decimal_places=0)

    def __str__(self):
        return self.title


# class UserManager(BaseUserManager):
#     def create_user(self, username, email, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email)
#         user.set_password(password)  # Используем встроенный метод для шифрования пароля
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, username, email, password=None):
#         user = self.create_user(username, email, password)
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user
#
# class User(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(max_length=50, unique=True)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=30)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#
#     USERNAME_FIELD = 'username'  # Поле, используемое для аутентификации
#     REQUIRED_FIELDS = ['email']  # Поля, которые должны быть указаны при создании суперпользователя
#
#     objects = UserManager()
#
#     def __str__(self):
#         return self.username
