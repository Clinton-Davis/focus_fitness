from django.test import TestCase
from home.views import *


class HomeViewTest(TestCase):

    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="home/index.html")

    def test_about_view(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="home/about.html")

    def test_terms_view(self):
        response = self.client.get('/terms/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="home/terms.html")

    def test_Privacy_view(self):
        response = self.client.get('/privacy/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="home/privacy.html")

    def test_contact_view(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name="home/contact.html")
