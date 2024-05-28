# Generated by Django 4.0.1 on 2024-02-04 16:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0002_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="title",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="images",
                to="places.place",
                verbose_name="Место",
            ),
        ),
    ]
