from django.db import models
from tinymce import models as tinymce_models


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField(blank=True)
    description_long = models.TextField(blank=True)
    coordinates = tinymce_models.HTMLField(blank=True)
    lng = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.title
