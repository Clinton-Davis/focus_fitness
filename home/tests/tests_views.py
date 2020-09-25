from django.test import TestCase
from django.urls import reverse
from home.views import *


class TestHomeViews(TestCase):

    def test_index_view_GET(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('sales_items' in resp.context)
        self.assertTemplateUsed(resp, template_name="home/index.html")

    def test_about_view_GET(self):
        resp = self.client.get(reverse('about'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name="home/about.html")

    def test_terms_view_GET(self):
        resp = self.client.get(reverse('terms'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name="home/terms.html")

    def test_Privacy_view_GET(self):
        resp = self.client.get(reverse('privacy'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name="home/privacy.html")

    def test_contact_view_GET(self):
        resp = self.client.get(reverse('contact'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name="home/contact.html")


class TestIndexContext(TestCase):

    def test_display_items_GET(self):
        resp = self.client.get(reverse('home'))
        self.assertTrue('sales_items' in resp.context)

    def test_current_membership_GET(self):
        resp = self.client.get(reverse('home'))
        self.assertTrue('current_membership' in resp.context)

    def test_programs_GET(self):
        resp = self.client.get(reverse('home'))
        self.assertTrue('programs' in resp.context)

    def test_feature_blog_GET(self):
        resp = self.client.get(reverse('home'))
        self.assertTrue('feature_blog' in resp.context)
