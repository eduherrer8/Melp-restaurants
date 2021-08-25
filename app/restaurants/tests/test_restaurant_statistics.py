from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APITestCase


class TestRestarurantStatistics(APITestCase):

    fixtures = (
        "tests_data/restaurants.json",
    )

    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        cls.url = reverse("api:statistics")

    def test_happy_path(self):
        center_x = -99.1246991701265
        center_y = 19.439100216425
        radius = 150
        url = (
            f"{self.url}?latitude={center_y}&longitude={center_x}"
            f"&radius={radius}"
        )
        request = self.client.get(url)
        self.assertEqual(request.status_code, status.HTTP_200_OK)
        expected = {'count': 2, 'avg': 1.0, 'std': 0.0}
        self.assertEqual(expected, request.data)

    def test_no_info(self):
        request = self.client.get(self.url)
        expected = {}
        self.assertEqual(expected, request.data)

    def test_bad_info(self):
        center_x = "-99.1a46991701265"
        center_y = "19.4a39100216425"
        radius = 150
        url = (
            f"{self.url}?latitude={center_y}&longitude={center_x}"
            f"&radius={radius}"
        )
        request = self.client.get(url)
        expected = {}
        self.assertEqual(expected, request.data)

    def test_no_results(self):
        center_x = -50.146991701265
        center_y = 50.439100216425
        radius = 150
        url = (
            f"{self.url}?latitude={center_y}&longitude={center_x}"
            f"&radius={radius}"
        )
        request = self.client.get(url)
        expected = {'avg': None, 'count': 0, 'std': None}
        self.assertEqual(expected, request.data)
