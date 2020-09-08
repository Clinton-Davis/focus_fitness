from django.test import TestCase
from django.urls import reverse
from products.views import *


class TestProduct(TestCase):

    fixtures = [
        'memberships.json',
        'user.json',
        'products.json',
    ]

    def test_products_get(self):
        product = Product.objects.get(id=7)
        url = reverse('products:products')
        responce = self.client.get(url)
        self.assertEqual(responce.status_code, 200)
        self.assertContains(responce, product.name)

    def test_views_contains_products_get(self):
        product = Product.objects.get(id=7)
        url = reverse('products:products')
        responce = self.client.get(url)
        self.assertContains(responce, product.name)
