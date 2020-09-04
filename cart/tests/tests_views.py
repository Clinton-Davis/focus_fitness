from django.test import TestCase, Client
from django.urls import reverse
from cart.views import *


class CartViewTests(TestCase):

    def test_cart_list_view_GET(self):
        resp = self.client.get(reverse('cart_view'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='cart/cart.html')

    # def test_add_to_cart_GET(self):
    #     resp = self.client.get(reverse('cart_view'))
    #     expected_url = reverse('products:products')
    #     self.assertEqual(resp.status_code, 200)
    #     self.assertRedirects(resp, expected_url,
    #                          )
    #     # self.assertTrue('category' in resp.context)
