from django.test import TestCase, Client
from django.urls import reverse
from home.views import *
from products.models import Product


class TestHomeViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('home')
        self.about_url = reverse('about')
        self.terms_url = reverse('terms')
        self.privacy_url = reverse('privacy')
        self.contact_url = reverse('contact')

    def test_index_view_GET(self):
        resp = self.client.get(self.index_url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name="home/index.html")

    def test_about_view_GET(self):
        resp = self.client.get(self.about_url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name="home/about.html")

    def test_terms_view_GET(self):
        resp = self.client.get(self.terms_url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name="home/terms.html")

    def test_Privacy_view_GET(self):
        resp = self.client.get(self.privacy_url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name="home/privacy.html")

    def test_contact_view_GET(self):
        resp = self.client.get(self.contact_url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name="home/contact.html")
