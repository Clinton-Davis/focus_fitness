from django.contrib.auth.models import User
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from memberships.models import *
from memberships.views import *


class TestMembershipsViews(TestCase):
    fixtures = [
        'member-memberships.json',
        'usermembership.json',
        'user.json',
    ]

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="tester", email="testing@test.com", password="testing12345")

    def test_membershipselectview(self):
        user = self.client.login(
            email="testing@test.com", password="testing12345")
        resp = self.client.get(reverse("memberships:select-membership"))
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('current_membership' in resp.context)
