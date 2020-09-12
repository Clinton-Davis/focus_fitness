
from django.contrib.auth.models import User
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from programs.models import Program, Workout
from programs.views import *


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
        self.assertEqual(resp.status_code, 200)

    def test_logged_in_user_program_detail_view_(self):
        user = self.client.login(
            email="testing@test.com", password="testing12345")
        program = Program.objects.get(id=2)
        program_slug = program.slug
        resp = self.client.get(f'/programs/{program_slug}')
        self.assertEqual(resp.status_code, 200)

    def test_logged_out_user_program_detail_view_(self):
        program = Program.objects.get(id=2)
        program_slug = program.slug
        resp = self.client.get(f'/programs/{program_slug}')
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(
            resp, f"/accounts/login/?next=/programs/{program_slug}")


class TestWorkoutDetailView(TestCase):

    fixtures = ['member-memberships.json', 'programs.json', ]

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="tester", email="testing@test.com", password="testing12345")

    def test_logged_in_user_workout_detail_view_(self):
        user = self.client.login(
            email="testing@test.com", password="testing12345")
        program = Program.objects.get(id=2)
        workout = Workout.objects.get(id=2)
        program_slug = program.slug
        workout_slug = workout.slug
        resp = self.client.get(f'/programs/{program_slug}/{workout_slug}')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(
            resp, template_name="programs/workout_detail.html")

    def test_logged_out_user_workout_detail_view_(self):
        program = Program.objects.get(id=2)
        workout = Workout.objects.get(id=2)
        program_slug = program.slug
        workout_slug = workout.slug
        resp = self.client.get(f'/programs/{program_slug}/{workout_slug}')
        self.assertRedirects(
            resp, f"/accounts/login/?next=/programs/{program_slug}/{workout_slug}",
            status_code=302)
