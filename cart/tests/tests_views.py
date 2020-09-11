from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product
from cart.views import *


class CartViewTests(TestCase):

    def test_cart_list_view_GET(self):
        resp = self.client.get(reverse('cart_view'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='cart/cart.html')


class Add_To_Cart(TestCase):

    fixtures = ['products_products.json',
                'products_catogerys']

    def test_add_to_cart_views(self):
        resp = self.client.get(reverse('cart_view'))
        print(resp.context)
        self.assertEqual(resp.status_code, 200)

    def test_add_to_cart_views(self):
        product = Product.objects.get(id=5)

        # resp = self.client.get('/cart/add/5/')
