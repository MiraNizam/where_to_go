# Generated by Django 5.0.6 on 2024-06-05 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0008_rename_description_long_place_long_description_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="place",
            name="title",
            field=models.CharField(
                max_length=200, unique=True, verbose_name="Название места"
            ),
        ),
    ]