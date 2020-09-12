from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.contrib.messages import get_messages
from django.urls import reverse
from marketing.views import *
from marketing.forms import NewLetterEmailSignupForm


class TestMarketingViews(TestCase):

    fixtures = [
        'member-memberships.json',
        'user.json',
        'marketing.json',
    ]

    def test_marketing_views_get(self):
        resp = self.client.get(reverse('marketing:newsubs'))
        self.assertEqual(resp.status_code, 302)

    def test_marketing_views_get(self):
        form = NewLetterEmailSignupForm()
        resp = self.client.post(
            '/marketing/newsubs/', {'email': 'newmail.com', })
        self.assertFalse(form.is_valid())
        self.assertEqual(resp.status_code, 302)

    def test_newsletter_sub_new(self):
        # user = User.objects.get(id=2)
        resp = self.client.post(
            '/marketing/newsubs/', {'email': 'new@mail.com', })
        messages = list(get_messages(resp.wsgi_request))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "Thank you for joining our mailing list")

    def test_newsletter_sub_resub(self):
        user = User.objects.get(id=13)
        email = user.email
        resp = self.client.post(
            '/marketing/newsubs/', {'email': f'{email}', })
        messages = list(get_messages(resp.wsgi_request))
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]),
                         "You are already part of the News Letter mailing list")
