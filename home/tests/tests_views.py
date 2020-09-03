from django.test import TestCase
from django.urls import reverse
from home.views import *


class TestHomeView(TestCase):

    def test_index_view(self):
        url = reverse('home')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name="home/index.html")

    def test_about_view(self):
        url = reverse('about')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name="home/about.html")

    def test_terms_view(self):
        url = reverse('terms')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name="home/terms.html")

    def test_Privacy_view(self):
        url = reverse('privacy')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name="home/privacy.html")

    def test_contact_view(self):
        url = reverse('contact')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name="home/contact.html")
