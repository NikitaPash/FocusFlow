from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path(
        "password-reset-done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="user_auth/forgot_password/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        views.MyPasswordResetConfirmView.as_view(
            template_name="user_auth/forgot_password/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="user_auth/forgot_password/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
