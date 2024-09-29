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
    rating_count = models.IntegerField(default=0)
    total_rating = models.FloatField(default=0)
    pub_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(null=False, blank=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(trans(self.title), allow_unicode=True)
        super().save(*args, **kwargs)


class ProjectRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("user", "project")


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
