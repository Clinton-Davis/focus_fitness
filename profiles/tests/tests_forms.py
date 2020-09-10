from django.test import TestCase
from profiles.forms import UserProfileAddressForm
from profiles.models import UserProfile


class TestUserProfileAddressForm(TestCase):
    """Testing that the nothing on the profile default is required"""

    def test_user_profile_address_form_not_required(self):
        valid_data = {
            'default_email': '',
            'default_phone_number': '',
            'default_street_address1': '',
            'default_street_address2': '',
            'default_town_or_city': '',
            'default_postcode': '',
            'default_county': '',
            'default_country': ''
        }
        form = UserProfileAddressForm(data=valid_data)
        self.assertTrue(form.is_valid())
        self.assertFalse(form.errors)

    def test_user_profile_address_form_metaclass(self):
        """ Testing the user filed is excluded in the profile UserProfileAddressForm"""
        form = UserProfileAddressForm()
        self.assertEqual(form.Meta.exclude, ('user',))
