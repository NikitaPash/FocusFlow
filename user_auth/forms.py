from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordResetForm,
    SetPasswordForm,
)
from user_auth.models import User
from django.contrib.auth import authenticate

from django import forms
from django.forms.widgets import PasswordInput, TextInput, EmailInput, CheckboxInput


class CreateUserForm(UserCreationForm):
    username = forms.CharField(
        widget=TextInput(
            attrs={
                "type": "text",
                "autocomplete": "username",
                "class": "form-control",
                "name": "username",
                "id": "InputUsername",
                "placeholder": "Enter username",
            }
        )
    )
    email = forms.EmailField(
        widget=EmailInput(
            attrs={
                "type": "email",
                "autocomplete": "email",
                "class": "form-control",
                "name": "email",
                "id": "InputEmail",
                "placeholder": "Enter email",
            }
        )
    )
    password1 = forms.CharField(
        widget=PasswordInput(
            attrs={
                "type": "password",
                "autocomplete": "new-password",
                "class": "form-control",
                "name": "password1",
                "id": "InputPassword",
                "placeholder": "Enter password",
            }
        )
    )
    password2 = forms.CharField(
        widget=PasswordInput(
            attrs={
                "type": "password",
                "autocomplete": "new-password",
                "class": "form-control",
                "name": "password2",
                "id": "InputPasswordConfirm",
                "placeholder": "Confirm password",
            }
        )
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class LoginForm(AuthenticationForm):

    username = forms.CharField(required=False)

    email = forms.EmailField(
        widget=EmailInput(
            attrs={
                "type": "email",
                "autocomplete": "email",
                "class": "form-control",
                "name": "email",
                "id": "InputLoginEmail",
                "placeholder": "Enter email",
            }
        )
    )
    password = forms.CharField(
        required=False,
        widget=PasswordInput(
            attrs={
                "type": "password",
                "autocomplete": "current-password",
                "class": "form-control",
                "name": "password",
                "id": "InputPassword",
                "placeholder": "Enter password",
            }
        ),
    )

    remember_me = forms.BooleanField(
        required=False,
        widget=CheckboxInput(
            attrs={
                "class": "form-check-input",
                "type": "checkbox",
                "id": "RememberCheck",
            }
        ),
    )

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            self.user_cache = authenticate(
                self.request, username=email, password=password
            )
            if self.user_cache is None:
                raise forms.ValidationError("Invalid email or password.")
            elif not self.user_cache.is_active:
                raise forms.ValidationError("This account is inactive.")

        return self.cleaned_data

    def get_user(self):
        return self.user_cache


class MyPasswordResetForm(PasswordResetForm):
    email = forms.CharField(
        label="Email",
        max_length=254,
        required=True,
        widget=forms.EmailInput(
            attrs={
                "autocomplete": "email",
                "class": "form-control",
                "name": "email",
                "id": "InputResetEmail",
                "placeholder": "Email address",
            }
        ),
    )


class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "type": "password",
                "class": "form-control",
                "name": "new_password1",
                "id": "InputPassword",
                "placeholder": "New password",
            }
        ),
    )
    new_password2 = forms.CharField(
        label="New password confirmation",
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "type": "password",
                "class": "form-control",
                "name": "new_password2",
                "id": "InputPasswordConfirm",
                "placeholder": "Confirm password",
            }
        ),
    )
