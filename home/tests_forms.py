from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):

    def test_name_is_required(self):
        form = ContactForm({'name': ''})

    def test_email_is_required(self):
        form = ContactForm({'email': ''})

    def test_message_is_required(self):
        form = ContactForm({'message': ''})

        self.assertFalse(form.is_valid())
