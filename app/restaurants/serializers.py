from rest_framework import serializers

from restaurants.models import Restaurant
from django.contrib.gis.geos import Point


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        exclude = ("point", )

    def create(self, validated_data):
        validated_data["point"] = Point(
            x=validated_data["lng"],
            y=validated_data["lat"],
            srid=4326
        )
        return Restaurant.objects.create(**validated_data)

    def update(self, instance, validated_data):
        validated_data["point"] = Point(
            x=validated_data.get("lng", instance.point.x),
            y=validated_data.get("lat", instance.point.y),
            srid=4326
        )
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
