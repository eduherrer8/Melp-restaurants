from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from restaurants.views import RestaurantView
from restaurants.views import Statistics

restaurant_router = routers.SimpleRouter()
restaurant_router.register(
    "restaurants", RestaurantView, basename="restaurants")


app_name = "restaurants"

urlpatterns = [
    path("restaurants/statistics", Statistics.as_view(), name="statistics"),
    path("", include(restaurant_router.urls)),
]
