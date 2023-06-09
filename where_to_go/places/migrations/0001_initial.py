# Generated by Django 4.1.7 on 2023-03-25 08:50

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Place",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("description_short", models.CharField(max_length=200)),
                ("description_long", models.TextField(blank=True)),
                ("coordinates", tinymce.models.HTMLField()),
                ("lng", models.FloatField()),
                ("lat", models.FloatField()),
            ],
        ),
    ]
