from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from restaurants.models import Restaurant


class TestRestarurantServices(APITestCase):

    fixtures = (
        "tests_data/restaurants.json",
    )

    @classmethod
    def setUpTestData(cls):
        cls.restaurant = Restaurant.objects.last()
        cls.client = APIClient()
        cls.urls = {
            "list": reverse("api:restaurants-list"),
            "retrieve":
                reverse("api:restaurants-detail",
                        kwargs={"pk": cls.restaurant.pk}),
        }

    def test_list(self):
        request = self.client.get(self.urls["list"])
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(request.data["count"], Restaurant.objects.count())

    def test_post(self):
        before = Restaurant.objects.count()
        data = {
            "id": "851f799f-0852-439e-b9b2-df92c43e7674",
            "rating": 1,
            "name": "Barajas, Bahena and Kano",
            "site": "https://federico.com",
            "email": "Anita_Mata71@hotmail.com",
            "phone": "534 814 204",
            "street": "82247 Mariano Entrada",
            "city": "Mérida Alfredotown",
            "state": "Durango",
            "lat": 19.4400570537131,
            "lng": -99.1270470974249
        }
        request = self.client.post(self.urls["list"], data)
        self.assertEqual(request.status_code, status.HTTP_201_CREATED)
        self.assertEqual(before + 1, Restaurant.objects.count())
        self.assertTrue(Restaurant.objects.filter(pk=data["id"]).exists())

    def test_post_missing_info(self):
        before = Restaurant.objects.count()
        request = self.client.post(self.urls["list"], {})
        self.assertEqual(
            str(request.data["site"][0]), "This field is required.")
        self.assertEqual(request.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(before, Restaurant.objects.count())

    def test_delete(self):
        before = Restaurant.objects.count()
        request = self.client.delete(self.urls["retrieve"])
        self.assertEqual(request.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(before - 1, Restaurant.objects.count())

    def test_retrieve(self):
        request = self.client.get(self.urls["retrieve"])
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.assertEqual(request.data["id"], self.restaurant.id)
        self.assertEqual(request.data["rating"], self.restaurant.rating)

    def test_put(self):
        data = self.client.get(self.urls["retrieve"]).data
        data["rating"] = 4
        request = self.client.put(self.urls["retrieve"], data)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.restaurant.refresh_from_db()
        self.assertEqual(self.restaurant.rating, data["rating"])

    def test_patch(self):
        data = {'lat': 20.439100216425, 'lng': -98.1246991701265}
        request = self.client.patch(self.urls["retrieve"], data)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        self.restaurant.refresh_from_db()
        self.assertEqual(self.restaurant.point.x, data["lng"])
        self.assertEqual(self.restaurant.point.y, data["lat"])
