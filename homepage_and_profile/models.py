from django.db import models

from user_auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.TextField(max_length=150, blank=True)
    bio = models.TextField(max_length=160, blank=True)
    website = models.URLField(max_length=200, blank=True)
    github = models.URLField(max_length=200, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)
    email = models.EmailField(max_length=254, blank=True)
