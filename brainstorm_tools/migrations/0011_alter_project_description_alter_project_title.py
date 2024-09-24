# Generated by Django 5.0.7 on 2024-09-21 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("brainstorm_tools", "0010_alter_project_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="description",
            field=models.TextField(max_length=150),
        ),
        migrations.AlterField(
            model_name="project",
            name="title",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
