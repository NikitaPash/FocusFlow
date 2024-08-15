from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.views import PasswordResetView
from django.forms.widgets import PasswordInput, TextInput, EmailInput, CheckboxInput


class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(
        attrs={'type': "text", 'class': "form-control", 'name': "username", 'id': "InputUsername",
               'placeholder': "Enter username"}))
    email = forms.CharField(widget=EmailInput(
        attrs={'type': "email", 'class': "form-control", 'name': "email", 'id': "InputEmail",
               'placeholder': "Enter email"}))
    password1 = forms.CharField(widget=PasswordInput(
        attrs={'type': "password", 'class': "form-control", 'name': "password1", 'id': "InputPassword",
               'placeholder': "Enter password"}))
    password2 = forms.CharField(widget=PasswordInput(
        attrs={'type': "password", 'class': "form-control", 'name': "password2", 'id': "InputPasswordConfirm",
               'placeholder': "Confirm password"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=TextInput(attrs={'type': "text", 'class': "form-control", 'name': "username", 'id': "InputUsername",
                                'placeholder': "Enter username"}))
    password = forms.CharField(widget=PasswordInput(
        attrs={'type': "password", 'class': "form-control", 'name': "password", 'id': "InputPassword",
               'placeholder': "Enter password"}))

    remember_me = forms.BooleanField(required=False,
                                     widget=CheckboxInput(attrs={'class': "form-check-input", 'type': "checkbox",
                                                                 'id': "RememberCheck"}))


class MyPasswordResetForm(PasswordResetForm):
    email = forms.CharField(label="Email", max_length=254, required=True,
                            widget=forms.EmailInput(
                                attrs={"autocomplete": "email", 'class': "form-control", 'name': "email",
                                       'id': "InputEmail",
                                       'placeholder': "Email address"}))
