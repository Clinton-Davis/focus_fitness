from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class TestProfileViews(TestCase):

    fixtures = ['memberships.json', ]

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

    fixtures = ['memberships.json', ]

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="tester", email="testing@test.com", password="testing12345")

    def test_logged_in_Profile_shipping_view_(self):
        user = self.client.login(
            email="testing@test.com", password="testing12345")
        resp = self.client.get(reverse('profiles:shipping_details'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(
            resp, template_name="profiles/shipping_details.html")

    def test_logged_in_Profile_shipping_view_context_(self):
        user = self.client.login(
            email="testing@test.com", password="testing12345")
        resp = self.client.get(reverse('profiles:shipping_details'))
        self.assertTrue('user' in resp.context)

    def test_logged_out_user_Profile_shipping_view(self):
        resp = self.client.get(reverse('profiles:shipping_details'))
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(
            resp, "/accounts/login/?next=/profile/shipping_details/")

    def test_profile_shipping_view_post(self):
        user = self.client.login(
            email="testing@test.com", password="testing12345")
        resp = self.client.post(
            '/profile/profile_details/', {' default_phone_number': '5', })
        self.assertEqual(resp.status_code, 200)


class Test_profile_subscriptions(TestCase):

    fixtures = ['memberships.json', ]

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

    fixtures = ['memberships.json', ]

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
