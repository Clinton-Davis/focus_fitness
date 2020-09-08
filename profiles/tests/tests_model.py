from django.test import TestCase
from django.contrib.auth import get_user_model
from memberships.models import Membership


User = get_user_model()


class UserProfileTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            "Tracytesting", "testing@testing.com", "testing12345")

    def setUp(self):
        self.user = User.objects.get(email="testing@testing.com")

    def test_create_user(self):
        userprofile = User.objects.create(
            user=self.user,
        )
        self.assertTrue(isinstance(userprofile, User))
