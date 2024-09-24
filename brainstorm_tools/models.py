from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from trans import trans

from user_auth.models import User


class Project(models.Model):
    user = models.ForeignKey(User, related_name="projects", on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=150)
    detailed_description = models.TextField(max_length=2000)
    pub_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=False, blank=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(trans(self.title), allow_unicode=True)
        super().save(*args, **kwargs)


class Feature(models.Model):
    project = models.ForeignKey(
        Project, related_name="features", on_delete=models.CASCADE
    )
    feature_name = models.CharField(max_length=100)


class SubFeature(models.Model):
    feature = models.ForeignKey(
        Feature, related_name="subfeatures", on_delete=models.CASCADE
    )
    subfeature_name = models.CharField(max_length=100)
