from django.contrib.messages import get_messages
from django.test import TestCase, Client
from django.urls import reverse
from products.models import Product
from cart.views import *


class CartViewsTests(TestCase):

    fixtures = ['products_products.json',
                'products_catogerys']

    def test_cart_list_view_GET(self):
        resp = self.client.get(reverse('cart_view'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='cart/cart.html')

    def test_add_to_cart_view(self):
        resp = self.client.get(reverse('cart_view'))
        self.assertEqual(resp.status_code, 200)

    def test_add_item_qty_size_to_add_cart_views(self):
        resp = self.client.post(
            '/cart/add/5/', {'quantity': '7', 'redirect_url': 'cart_view', 'product_size': 'm'})
        messages = list(get_messages(resp.wsgi_request))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         'Added size M - Navy Blue Mens Jacket')

    def test_add_item_qty_to_add_cart_views(self):
        resp = self.client.post(
            '/cart/add/4/', {'quantity': '4', 'redirect_url': 'cart_view', })
        messages = list(get_messages(resp.wsgi_request))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         'Added Gold Standard 100% Whey Protein')

    def test_add_item_qty_size_to_adjust_cart_views(self):
        resp = self.client.post(
            '/cart/adjust/8/', {'quantity': '7'})
        messages = list(get_messages(resp.wsgi_request))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Updated Red Men's Jacket quantity to 7")
