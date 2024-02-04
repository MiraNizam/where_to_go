from django.shortcuts import render, get_object_or_404
from .models import Place, Image


def index(request):
    places = Place.objects.all()

    places_features = []
    for place in places:
        properties = {
            "title": place.title,
            "placeId": place.pk,
            "detailsUrl": place_details(request, place.pk)} # понимаю, что неверно, но не знаю как правильно
        features = {"type": "Feature",
                    "geometry":
                        {"type": "Point",
                         "coordinates": [place.longitude, place.latitude]
                         },
                    "properties": properties
                    }
        places_features.append(features)
    data = {"type": "FeatureCollection", "features": places_features}
    return render(request, "index.html", context=data)


def place_details(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_descriptions = {
        "title": place.title,
        "imgs": [image.url for image in place.images], # тут тоже что-то не так
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {"lng": place.longitude,
                        "lat": place.latitude
                        }
    }
    # print(place_descriptions)
    return render(request, "index.html", context=place_descriptions)


