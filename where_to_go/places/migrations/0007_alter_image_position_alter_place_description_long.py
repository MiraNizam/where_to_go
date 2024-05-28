# Generated by Django 4.0.1 on 2024-04-06 09:02

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("places", "0006_alter_image_options_image_position"),
    ]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="position",
            field=models.PositiveIntegerField(
                db_index=True, default=0, verbose_name="Позиция картинки"
            ),
        ),
        migrations.AlterField(
            model_name="place",
            name="description_long",
            field=tinymce.models.HTMLField(
                blank=True, verbose_name="Полное описание места"
            ),
        ),
    ]
