from django.test import TestCase
from checkout.models import *


class TestCheckoutModels(TestCase):

    fixtures = [
        'memberships.json',
        'user.json',
        'products.json',
        'blog.json',
    ]

    @classmethod
    def setUpTestData(cls):
        Order.objects.create(
            order_number=000,
            full_name="Testing Mc Testalot",
            email='testing@tesing.com',
            phone_number='987766544667',
            country='IRE',
            town_or_city='Testing Town',
            street_address1='Testing Street',
            delivery_cost='0',
        )

    def test_Checkout_name(self):
        order_number = Order.objects.get(id=1)
        self.assertEqual(Order.order_number, 000)
