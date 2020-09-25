from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.contrib import messages
from django.test import TestCase, Client
from django.urls import reverse
from products.views import *


class TestProduct(TestCase):

    fixtures = [
        'memberships.json',
        'user.json',
        'products.json',
    ]

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="tester", email="testing@test.com", password="testing12345")

    def setUp(self):
        user = self.client.login(
            email="testing@test.com", password="testing12345")

    def test_products_get(self):
        product = Product.objects.get(id=4)
        resp = self.client.get(reverse('products:products'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, product.name)

    def test_views_contains_products_get(self):
        product = Product.objects.get(id=4)
        resp = self.client.get(reverse('products:products'))
        self.assertContains(resp, product.name)

    def test_product_comment_view_vaild_post(self):
        user = User.objects.get(id=2)
        resp = self.client.post(
            '/products/5/', {'rating': '4', 'content': 'Testing'})
        self.assertRedirects(resp, "/products/5/")
        self.assertEqual(resp.status_code, 302)

    def test_product_sort_asc_post(self):
        resp = self.client.get(
            '/products/?', {'sort': 'name', 'direction': 'asc'})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['sorting'], 'name_asc')

    def test_product_sort_desc_post(self):
        resp = self.client.get(
            '/products/?', {'sort': 'name', 'direction': 'desc'})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['sorting'], 'name_desc')

    def test_product_sort_category_asc_post(self):
        resp = self.client.get(
            '/products/?', {'sort': 'category', 'direction': 'asc'})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['sorting'], 'category_asc')

    def test_product_sort_category_desc_post(self):
        resp = self.client.get(
            '/products/?', {'sort': 'category', 'direction': 'desc'})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['sorting'], 'category_desc')

    def test_product_search_post(self):
        resp = self.client.get(
            '/products/?', {'q': 'jeans'})
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['search_term'], 'jeans')

    def test_product_search_Error_message_post(self):
        resp = self.client.get(
            '/products/?', {'q': ''})
        messages = list(get_messages(resp.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Sorry! No Input? Try again Please")
