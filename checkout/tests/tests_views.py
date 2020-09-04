from django.test import TestCase, Client
from django.urls import reverse
from profiles.models import UserProfile


class TestCheckoutViews(TestCase):

    def test_get(self):
        url = reverse('checkout:checkout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
