from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone

from user_auth.models import User


class Project(models.Model):
    user = models.ForeignKey(User, related_name="projects", on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(max_length=350, unique=True)
    pub_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=False, blank=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.user.username}_{self.title}')
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
