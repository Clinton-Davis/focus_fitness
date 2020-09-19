from django.test import TestCase
from checkout.models import Order


class TestCheckoutModels(TestCase):

    fixtures = [
        'member-memberships.json',
        'user.json',
        'products.json',
    ]

    @classmethod
    def setUpTestData(cls):
        Order.objects.create(
            order_number=000,
            full_name="Testing Mc Testalot",
            email='testing@tesing.com',
            phone_number=987766544667,
            country='IRE',
            town_or_city='Testing Town',
            street_address1='Testing Street',

        )

    def test_Checkout_details(self):
        order = Order.objects.get(id=1)
        self.assertEqual(order.full_name, 'Testing Mc Testalot')
        self.assertEqual(order.email, 'testing@tesing.com')
        self.assertEqual(order.town_or_city, 'Testing Town')

    def test_Checkout_generate_order_number(self):
        order = Order.objects.get(id=1)
        self.assertFalse(order.order_number == 000)
