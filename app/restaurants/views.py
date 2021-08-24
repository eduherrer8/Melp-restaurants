from rest_framework.viewsets import ModelViewSet

from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer


class RestaurantView(ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
