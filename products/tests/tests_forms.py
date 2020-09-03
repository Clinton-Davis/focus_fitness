from django.test import TestCase
from products.forms import ProductCommentForm


class TestProductCommentForm(TestCase):

    def test_rating_is_required(self):
        form = ProductCommentForm({'rating': ''})
        self.assertFalse(form.is_valid())

    def test_content_is_required(self):
        form = ProductCommentForm({'content': 'Testing Context'})
        self.assertTrue(form.is_valid)
