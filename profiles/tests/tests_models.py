from django.test import TestCase
from django.contrib.auth.models import User


class UserProfileTest(TestCase):

    fixtures = [
        'member-memberships.json',
        'user.json'
    ]

    def test_create_user(self):
        userprofile = User.objects.create_user(
            email='testing@testing.com', username='tester')
        self.assertTrue(isinstance(userprofile, User))

    def setUp(self):
        self.user = User.objects.get(id=2)

    def test_user_string(self):
        userprofile = User.objects.get(id=2)
        self.assertEqual(userprofile.__str__(),  self.user.username)
