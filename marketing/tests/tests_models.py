from django.test import TestCase
from marketing.models import *


class TestMarketingModels(TestCase):

    def test_Checkout_details(self):
        NewsLetterSignups.objects.create(email='testing@tesing.com',)
        new_email = NewsLetterSignups.objects.get(id=1)
        self.assertEqual(new_email.email, 'testing@tesing.com')
