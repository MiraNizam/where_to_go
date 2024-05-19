from json.decoder import JSONDecodeError
from urllib.parse import urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Image, Place


class Command(BaseCommand):
    help = "Load files with places into the database"

    def add_arguments(self, parser):
        parser.add_argument(
            "json_link",
            type=str,
            help="Provide a link to the JSON file with location information",
        )

    def handle(self, *args, **options):
        response = requests.get(options["json_link"])
        response.raise_for_status()
        place_description = response.json()
        try:
            place, created = Place.objects.get_or_create(
                title=place_description["title"],
                description_short=place_description["description_short"],
                description_long=place_description["description_long"],
                longitude=place_description["coordinates"]["lng"],
                latitude=place_description["coordinates"]["lat"],
            )

            if created:
                for image_number, image_link in enumerate(place_description["imgs"]):
                    response = requests.get(image_link)
                    response.raise_for_status()
                    image_name = urlparse(image_link).path.split("/")[-1]
                    image_content = ContentFile(response.content, name=image_name)
                    Image.objects.create(
                        place=place, image=image_content, position=image_number
                    )

        except (FileNotFoundError, JSONDecodeError):
            raise ValueError(
                "The file was not found or the file structure does not match what is stated in the README, "
                "please go back and check the file from the link."
            )
