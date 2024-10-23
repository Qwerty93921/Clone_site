from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    author = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(null=False, blank=False, max_digits=15, decimal_places=2)
    # decimal_places = 2 - значит 2 цифры после запятой, ВСЕГО 10 цифр

    def __str__(self):
        return self.title


class Car(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    seller = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(null=False, blank=False, max_digits=20, decimal_places=2)

    def __str__(self):
        return self.title


class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=100)
