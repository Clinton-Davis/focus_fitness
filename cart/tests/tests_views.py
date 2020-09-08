from django.test import TestCase, Client
from django.urls import reverse
from cart.views import *


class CartViewTests(TestCase):

    def test_cart_list_view_GET(self):
        resp = self.client.get(reverse('cart_view'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='cart/cart.html')
