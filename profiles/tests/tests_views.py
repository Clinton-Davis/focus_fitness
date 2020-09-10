from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.contrib.messages import get_messages
from django.urls import reverse
from profiles.models import UserProfile


class TestProfileViews(TestCase):

    fixtures = ['member-memberships.json', ]

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="tester", email="testing@test.com", password="testing12345")

    def test_logged_in_user_Profile_view_(self):
        user = self.client.login(
            email="testing@test.com", password="testing12345")
        resp = self.client.get(reverse('profiles:profile'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name="profiles/profile.html")

    def test_logged_in_user_Profile_context_(self):
        user = self.client.login(
            email="testing@test.com", password="testing12345")
        resp = self.client.get(reverse('profiles:profile'))
        self.assertTrue('user_blog' in resp.context)
        self.assertTrue('profile' in resp.context)
        self.assertTrue('user_membership' in resp.context)
        self.assertTrue('user_subscription' in resp.context)
        self.assertTrue('orders' in resp.context)

    def test_logged_out_user_Profile_view_(self):
        resp = self.client.get(reverse('profiles:profile'))
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, "/accounts/login/?next=/profile/")


class TestProfileDetailViews(TestCase):

    fixtures = ['member-memberships.json', ]

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="tester", email="testing@test.com", password="testing12345")

    def test_logged_in_Profile_detail_view_(self):
        user = self.client.login(
            email="testing@test.com", password="testing12345")
        resp = self.client.get(reverse('profiles:profile_details'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(
            resp, template_name="profiles/profile_details.html")

    def test_logged_in_Profile_detail_view_context_(self):
        user = self.client.login(
            email="testing@test.com", password="testing12345")
        resp = self.client.get(reverse('profiles:profile_details'))
        self.assertTrue('user' in resp.context)
        self.assertTrue('orders' in resp.context)

    def test_logged_out_user_Profile_detail_view(self):
        resp = self.client.get(reverse('profiles:profile_details'))
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(
            resp, "/accounts/login/?next=/profile/profile_details/")

    def test_profile_details_view_post(self):
        user = self.client.login(
            email="testing@test.com", password="testing12345")
        resp = self.client.post(
            '/profile/profile_details/', {' default_phone_number': '5', })
        self.assertEqual(resp.status_code, 200)

    # def test_profile_details_message_post(self):
    #     resp = self.client.get(
    #         '/profile/profile_details/', {' default_phone_number': '5', })
    #     messages = list(resp.context['messages'])
    #     self.assertEqual(len(messages), 1)
    #     self.assertEqual(str(messages[0]),
    #                      "'Your Shipping details have been updated'")


class Test_profile_subscriptions(TestCase):

    fixtures = ['member-memberships.json', ]

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="tester", email="testing@test.com", password="testing12345")

    def test_logged_in_profile_subscriptions_view_(self):
        user = self.client.login(
            email="testing@test.com", password="testing12345")
        resp = self.client.get(reverse('profiles:profile_subscriptions'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'profiles/profile_subscriptions.html')

    def test_logged_out_profile_subscriptions_view_(self):
        resp = self.client.get(reverse('profiles:profile_subscriptions'))
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(
            resp, '/accounts/login/?next=/profile/profile_subscriptions/')

    def test_logged_in_user_profile_subscriptions_context_(self):
        user = self.client.login(
            email="testing@test.com", password="testing12345")
        resp = self.client.get(reverse('profiles:profile_subscriptions'))
        self.assertTrue('profile' in resp.context)
        self.assertTrue('user_membership' in resp.context)
        self.assertTrue('user_subscription' in resp.context)


class TestCancel_Sub_Confirm(TestCase):

    fixtures = ['member-memberships.json', ]

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="tester", email="testing@test.com", password="testing12345")

    def test_cancel_sub_confirm(self):
        user = self.client.login(
            email="testing@test.com", password="testing12345")
        resp = self.client.get(reverse('profiles:cancel_sub'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "profiles/cancel_sub_confirm.html")

    def test_logged_out_cancel_sub_confirm(self):
        resp = self.client.get(reverse('profiles:cancel_sub'))
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(
            resp, "/accounts/login/?next=/profile/cancel_sub_confirm/")


# right a profile detaiview post for address and get mmessage
