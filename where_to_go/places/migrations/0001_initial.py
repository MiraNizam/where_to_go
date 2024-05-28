# Generated by Django 4.0.1 on 2024-02-03 11:40

from django.db import migrations, models


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
                (
                    "title",
                    models.CharField(max_length=200, verbose_name="Название места"),
                ),
                (
                    "description_short",
                    models.TextField(blank=True, verbose_name="Краткое описание места"),
                ),
                (
                    "description_long",
                    models.TextField(blank=True, verbose_name="Полное описание места"),
                ),
                ("longitude", models.FloatField(verbose_name="Долгота")),
                ("latitude", models.FloatField(verbose_name="Широта")),
            ],
        ),
    ]
