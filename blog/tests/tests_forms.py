from django.test import TestCase
from blog.forms import BlogForm
from blog.models import Blog


class TestBlogForm(TestCase):

    fixtures = [

        'user.json',

    ]

    def test_blog_create_form(self):

        invalid_data = {
            "title": "testing",
            "content": "this is a test",
            "thumbnail": " "
        }
        form = BlogForm(data=invalid_data)
        form.is_valid()
        self.assertTrue(form.errors)
