from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.forms import ModelForm, CharField, TextInput, FileInput, BooleanField, EmailInput, EmailField, PasswordInput


class RegisterForm(UserCreationForm):
    username = CharField(max_length=16, min_length=3, required=True, widget=TextInput(attrs={'class': 'form-control'}))
    email = EmailField(max_length=30, required=True, widget=EmailInput(attrs={'class': 'form-control'}))
    password1 = CharField(required=True, widget=PasswordInput(attrs={'class': 'form'}))
    password2 = CharField(required=True, widget=PasswordInput(attrs={'class': 'form'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = CharField(max_length=16, min_length=3, required=True, widget=TextInput(attrs={'class': 'form-control'}))
    password = CharField(required=True, widget=PasswordInput(attrs={'class': 'form'}))

    class Meta:
        model = User
        fields = ('username', 'password')


