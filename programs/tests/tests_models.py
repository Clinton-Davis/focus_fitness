from django.contrib.auth.models import User
from django.test import TestCase
from programs.models import Program, Workout


class TestProgram(TestCase):

    fixtures = [
        'memberships.json',
        'user.json',
        'programs.json'
    ]

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="tester", email="testing@test.com", password="testing12345")

    def test_create_Program(self):
        new_program = Program.objects.create(
            slug='new_test_program',
            title="New test program",
            description="testing the prodgrams model",
            thumbnail='Its a pic',
        )
        self.assertTrue(isinstance(new_program, Program))

    def test_get_absolute_url(self):
        new_program = Program.objects.get(id=2)
        program_slug = new_program.slug
        self.assertEquals(new_program.get_absolute_url(),
                          f'/programs/{program_slug}')


class TestWorkoutModel(TestCase):

    fixtures = [
        'memberships.json',
        'user.json',
        'programs.json'
    ]

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="tester", email="testing@test.com", password="testing12345")

    def test_create_workout(self):
        new_workout = Workout.objects.create(
            slug='new_test_new_workout',
            title="New test new_workout",
            position=1,
            video_url='its a video',
            thumbnail='its a pic.jpg'
        )
        self.assertTrue(isinstance(new_workout, Workout))
