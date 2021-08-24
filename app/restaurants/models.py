from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Restaurant(models.Model):
    id = models.TextField(primary_key=True)
    rating = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(4), MinValueValidator(0)]
    )
    name = models.TextField()
    site = models.URLField()
    email = models.EmailField()
    phone = models.TextField()
    street = models.TextField()
    city = models.TextField()
    state = models.TextField()
    lat = models.FloatField()
    lng = models.FloatField()
    point = models.PointField(geography=True)
