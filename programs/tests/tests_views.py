
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from programs.models import Program

# Create your tests here.


class TestProgramsViews(TestCase):

    fixtures = ['member-memberships.json', 'programs.json', ]

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="tester", email="testing@test.com", password="testing12345")

    def test_logged_in_user_program_view_(self):
        user = self.client.login(
            email="testing@test.com", password="testing12345")
        resp = self.client.get(reverse('programs:list'))
        self.assertEqual(resp.status_code, 200)

    def test_logged_out_user_program_view_(self):
        resp = self.client.get(reverse('programs:list'))
        self.assertRedirects(resp, "/accounts/login/",
                             status_code=302, target_status_code=200)

    def test_logged_in_user_program_detail_view_(self):
        user = self.client.login(
            email="testing@test.com", password="testing12345")
        resp = self.client.get('/programs/strength-training')
        self.assertEqual(resp.status_code, 200)

    def test_logged_out_user_program_detail_view_(self):
        resp = self.client.get('/programs/strength-training')
        self.assertEqual(resp.status_code, 200)
