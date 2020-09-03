from django.test import TestCase, Client
# Create your tests here.
from django.urls import reverse
from memberships.models import Membership


class TestMembershipsViews(TestCase):
    fixtures = [
        'memberships.json',
        'user.json',
        'products.json',
    ]

    def setUp(self):
        self.client = Client()
        self.memberships_url = reverse('memberships:select-membership')

    def test_memberships_view_GET(self):
        resp = self.client.get(self.memberships_url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name="memberships.html")
