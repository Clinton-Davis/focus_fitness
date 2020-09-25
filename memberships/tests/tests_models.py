from django.contrib.auth.models import User
from django.test import TestCase
from memberships.models import Membership, UserMembership, Subscription


class TestUserMembership(TestCase):

    fixtures = [
        'memberships.json',
        'user.json',
        'programs.json'
    ]

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="tester", email="testing@test.com", password="testing12345")

    def setUp(self):
        self.user = User.objects.get(
            email="testing@test.com", username="tester")

    def test_create_usermembership(self):
        new_user_mem = UserMembership.objects.get(user=self.user,)
        self.assertTrue(isinstance(new_user_mem, UserMembership))

    def test_usermembership_string(self):
        new_user_mem = UserMembership.objects.get(user=self.user,)
        self.assertEqual(new_user_mem.__str__(), self.user.username)


# class TestSubscription(TestCase):

#     fixtures = [
#         'member-memberships.json',
#         'usermembership.json',
#         'user.json',
#         'programs.json'
#     ]

#     @classmethod
#     def setUpTestData(cls):
#         user = User.objects.get(id=2)
#         print(user.usermembership)

#     def setUp(self):
#         self.usermembership = UserMembership.objects.get(
#             membership=2, user=1, stripe_customer_id="stripe_id")

#     def test_create_Subscription(self):
#         new_user_sub = Subscription.objects.create(
#             user_membership=self.usermembership,
#             stripe_subscription_id="stripe_id647463")
#         self.assertTrue(isinstance(new_user_sub, UserMembership))

#     # def test_Subscription_string(self):
#     #     new_user_sub = Subscription.objects.get(user=self.user,)
#     #     self.assertEqual(new_user_sub.__str__(), self.user.username)
