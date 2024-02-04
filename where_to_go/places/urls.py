from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('place/<int:id>/', views.place_details, name='place_details')
]