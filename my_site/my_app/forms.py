from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User  # Указываем модель, с которой связана форма
        fields = ['username', 'email', 'password']  # Указываем поля для формы
