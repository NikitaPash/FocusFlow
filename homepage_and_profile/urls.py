from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("profile/<int:user_id>/", views.profile, name="profile"),
]
