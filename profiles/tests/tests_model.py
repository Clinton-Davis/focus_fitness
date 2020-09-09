from django.test import TestCase
from django.contrib.auth import get_user_model
from memberships.models import Membership, UserMembership


# class UserProfileTest(TestCase):

#     def test_create_user(self):
#         userprofile = User.objects.get(
#             user=self.user,)
#         self.assertTrue(isinstance(userprofile, User))
