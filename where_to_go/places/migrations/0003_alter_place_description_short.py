# Generated by Django 4.1.7 on 2023-03-25 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0002_alter_place_coordinates"),
    ]

    operations = [
        migrations.AlterField(
            model_name="place",
            name="description_short",
            field=models.TextField(blank=True),
        ),
    ]
