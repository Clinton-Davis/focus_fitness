from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from blog.models import *


User = get_user_model()


class TestCreateBlogModels(TestCase):
    """testing the creation on a blog """
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="tester", email="testing@test.com", password="testing12345")

    def setUp(self):
        self.user = User.objects.get(username="tester")

    def test_create_Blog(self):
        newblog = Blog.objects.create(
            title='newblog',
            author=self.user,
            category="testingCatergory",
            content='testing loads of stuff',
            slug='testing',
        )
        self.assertTrue(isinstance(newblog, Blog))


class TestBlog(TestCase):
    """Testing the blog details and get_absolute_url() """
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="tester", email="testing@test.com", password="testing12345")

    def setUp(self):
        self.user = User.objects.get(username="tester")

        newblog = Blog.objects.create(
            title='newblog',
            author=self.user,
            category="testingCatergory",
            content='testing loads of stuff',
            slug='testing',
        )

    def test_get_absolute_url(self):
        newblog = Blog.objects.get(id=1)
        self.assertEquals(newblog.get_absolute_url(), '/blog/testing/')

    def test_get_update_url(self):
        newblog = Blog.objects.get(id=1)
        self.assertEquals(newblog.get_absolute_url(), '/blog/testing/')

    def test_get_delete_url(self):
        newblog = Blog.objects.get(id=1)
        self.assertEquals(newblog.get_absolute_url(), '/blog/testing/')

    def test_get_like_url(self):
        newblog = Blog.objects.get(id=1)
        self.assertEquals(newblog.get_absolute_url(), '/blog/testing/')

    def test_get_blog_title(self):
        newblog = Blog.objects.get(id=1)
        self.assertTrue(newblog.title, 'newblog')

    def test_get_blog_author(self):
        newblog = Blog.objects.get(id=1)
        self.assertTrue(newblog.author, 'tester')

    def test_get_blog_category(self):
        newblog = Blog.objects.get(id=1)
        self.assertTrue(newblog.category, 'testingCatergory')
