from django.test import TestCase
from django.contrib.auth import get_user_model
from blog.forms import BlogForm
from blog.models import Blog
from memberships.models import Membership, UserMembership


User = get_user_model()


# class TestBlogForm(TestCase):

#     def test_blog_create_form(self):

#         invalid_data = {
#             "title": "testing",
#             "content": "this is a test",
#             "thumbnail": " "
#         }
#         form = BlogForm(data=invalid_data)
#         print(BlogForm)
#         form.is_valid()
#         self.assertTrue(form.errors)
