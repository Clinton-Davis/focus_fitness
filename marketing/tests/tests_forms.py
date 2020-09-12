from django.test import TestCase
from marketing.forms import NewLetterEmailSignupForm
from marketing.models import *


class TestMarketingForm(TestCase):

    def test_marketing_form_required(self):

        form = NewLetterEmailSignupForm({'email': ''})
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)
        self.assertIn('email', form.errors.keys())

    def test_marketing_form_metaclass(self):
        form = NewLetterEmailSignupForm()
        self.assertEqual(form.Meta.fields,
                         ('email',))
