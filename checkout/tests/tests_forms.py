from django.test import TestCase
from checkout.forms import OrderForm
from checkout.models import Order


class TestOrderForm(TestCase):

    def test_OrderForm_(self):
        invalid_data = {
            'order_number': '',
            'user_profile': '',
            'full_name': '',
            'email': '',
            'phone_number': '',
            'street_address1': '',
            'street_address2': '',
            'town_or_city': '',
            'postcode': '',
            'county': '',
            'country': ''
        }

        form = OrderForm(data=invalid_data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)
        self.assertIn('full_name', form.errors.keys())
        self.assertIn('email', form.errors.keys())
        self.assertIn('phone_number', form.errors.keys())
        self.assertIn('street_address1', form.errors.keys())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertIn('postcode', form.errors.keys())

    def test_OrderForm_form_metaclass(self):
        form = OrderForm()
        self.assertEqual(form.Meta.fields, (
            'full_name', 'email', 'phone_number',
            'street_address1', 'street_address2',
            'town_or_city', 'postcode', 'country',
            'county',))
