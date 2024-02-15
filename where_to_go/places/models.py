from django.db import models


class Place(models.Model):
    title = models.CharField('Название места', max_length=200)
    description_short = models.TextField('Краткое описание места', blank=True)
    description_long = models.TextField('Полное описание места', blank=True)
    longitude = models.FloatField('Долгота')
    latitude = models.FloatField('Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name="Место", related_name="images")
    image = models.ImageField('Картинка')

    def __str__(self):
        return f"{self.id} {self.place}"


    #
