# Generated by Django 5.0.7 on 2024-09-30 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("brainstorm_tools", "0022_project_total_rating"),
    ]

    operations = [
        migrations.AlterField(
            model_name="projectrating",
            name="rating",
            field=models.IntegerField(default=0),
        ),
    ]
