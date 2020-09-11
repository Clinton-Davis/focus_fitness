from django.test import TestCase, Client
from django.urls import reverse
from profiles.models import UserProfile


class TestCheckoutViews(TestCase):

    def test_Checkout_get(self):
        resp = self.client.get(reverse('checkout:checkout'))
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, "/products/")
