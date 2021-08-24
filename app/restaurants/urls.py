from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from restaurants.views import RestaurantView

restaurant_router = routers.SimpleRouter()
restaurant_router.register(
    "restaurants", RestaurantView, basename="restaurants")


app_name = "restaurants"

urlpatterns = [
    path("", include(restaurant_router.urls)),
]
