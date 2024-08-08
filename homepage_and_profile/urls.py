from django.urls import path
import homepage_and_profile.views as views

urlpatterns = [
    path('home/', views.home),
]
