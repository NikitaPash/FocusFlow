from django.db import models

from user_auth.models import User


class Project(models.Model):
    user = models.ForeignKey(User, related_name="projects", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=350)


class Feature(models.Model):
    project = models.ForeignKey(
        Project, related_name="features", on_delete=models.CASCADE
    )
    feature_name = models.CharField(max_length=255)


class SubFeature(models.Model):
    feature = models.ForeignKey(
        Feature, related_name="subfeatures", on_delete=models.CASCADE
    )
    subfeature_name = models.CharField(max_length=255)
