# Generated by Django 5.0.7 on 2024-09-29 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "brainstorm_tools",
            "0017_remove_project_rating_remove_project_rating_count_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="rating",
            field=models.IntegerField(default=0),
        ),
    ]
