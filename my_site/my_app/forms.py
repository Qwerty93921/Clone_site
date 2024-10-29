from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User  # Указываем модель, с которой связана форма
        fields = ['username', 'email', 'password']  # Указываем поля для формы
        widgets = {
            'password': forms.PasswordInput(), # Метод PasswordInput скрывает введенный пароль, изначально там тип "текст"
        }

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('Пользователь с таким именем уже существует')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('Пользователь с таким адресом электронной почты уже существует')
        return email

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.password = make_password(self.cleaned_data['password'])  # Зашифруем пароль
        if commit:
            user.save()
        return user
