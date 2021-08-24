from django.contrib.gis.measure import Distance
from django.contrib.gis.geos import Point
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.db.models import Count
from django.db.models import Avg
from django.db.models import StdDev

from restaurants.models import Restaurant
from restaurants.serializers import RestaurantSerializer


class RestaurantView(ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()


class Statistics(APIView):

    def get(self, request, format=None):
        latitude = self.request.query_params.get("latitude")
        longitude = self.request.query_params.get("longitude")
        radius = self.request.query_params.get("radius")
        query = {}
        try:
            if latitude and longitude and radius:
                query = Restaurant.objects.filter(
                    point__distance_lt=(
                        Point(x=float(longitude), y=float(latitude)),
                        Distance(m=float(radius))
                    )
                ).aggregate(
                    count=Count("*"), avg=Avg('rating'), std=StdDev('rating')
                )
            return Response(query)
        except Exception:
            return Response({})
