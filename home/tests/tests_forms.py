from django.test import TestCase
from home.forms import ContactForm


class TestContactForm(TestCase):

    def test_name_is_required(self):
        form = ContactForm({'name': 'Testing_name'})
        self.assertTrue(form.is_valid)

    def test_email_is_required(self):
        form = ContactForm({'email': ''})
        self.assertFalse(form.is_valid())

    def test_message_is_required(self):
        form = ContactForm({'message': ''})
        self.assertFalse(form.is_valid())
