from django.db import models

from user_auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.TextField(max_length=150)
    bio = models.TextField(max_length=160)
    website = models.URLField(max_length=200)
    github = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)
    email = models.EmailField(max_length=254)
