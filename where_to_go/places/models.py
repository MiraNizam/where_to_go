from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField("Название места", max_length=200, unique=True)
    short_description = models.TextField("Краткое описание места", blank=True)
    long_description = HTMLField("Полное описание места", blank=True)
    longitude = models.FloatField("Долгота")
    latitude = models.FloatField("Широта")

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        Place, on_delete=models.CASCADE, verbose_name="Место", related_name="images"
    )
    image = models.ImageField("Картинка")
    position = models.PositiveIntegerField(
        "Позиция картинки", default=0, db_index=True
    )

    class Meta:
        ordering = [
            "position",
        ]

    def __str__(self):
        return f"{self.position} {self.place}"
