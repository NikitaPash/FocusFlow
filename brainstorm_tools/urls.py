from django.urls import path

from . import views

urlpatterns = [
    path("create-project/", views.create_project, name="create_project"),
]
