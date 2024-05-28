from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Image, Place


def index(request):
    places = Place.objects.all()

    places_features = []
    for place in places:

        properties = {
            "title": place.title,
            "placeId": place.id,
            "detailsUrl": reverse(place_details, kwargs={"place_id": place.id}),
        }
        features = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude],
            },
            "properties": properties,
        }
        places_features.append(features)
    context = {"type": "FeatureCollection", "features": places_features}
    return render(request, "index.html", context={"places": context})


def place_details(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_descriptions = {
        "title": place.title,
        "imgs": [image.image.url for image in place.images.all()],
        "description_short": place.short_description,
        "description_long": place.long_description,
        "coordinates": {"lng": place.longitude, "lat": place.latitude},
    }
    return JsonResponse(
        place_descriptions, json_dumps_params={"ensure_ascii": False, "indent": 2}
    )
