from django.test import TestCase, Client
from django.urls import reverse
from blog.views import *
from blog.models import *


class TestBlogViews(TestCase):
    fixtures = [
        'memberships.json',
        'user.json',
        'products.json',
        'blog.json',
    ]

    def test_blog_list_view_GET(self):
        resp = self.client.get(reverse('blog:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='blog/blog_list.html')
        self.assertTrue('feature_blog' in resp.context)
        self.assertTrue('category_menu' in resp.context)
        self.assertTrue('all_blogs' in resp.context)

    def test_blog_search_view_GET(self):
        resp = self.client.get(reverse('blog:search'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='blog/blog_search.html')

    def test_blog_create_view_GET(self):
        resp = self.client.get(reverse('blog:create'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='blog/blog_form.html')
        self.assertTrue('view_type' in resp.context)

    def test_blog_category_view_GET(self):
        resp = self.client.get('/blog/category/Strength%20Training/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(
            resp, template_name='blog/blog_categories.html')
        self.assertTrue('category' in resp.context)
        self.assertTrue('category_blogs' in resp.context)
        self.assertTrue('category_menu' in resp.context)
        self.assertTrue('all_blogs' in resp.context)

    def test_blog_update_view_GET(self):
        resp = self.client.get('/blog/testing/update/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='blog/blog_form.html')
        self.assertTrue('view_type' in resp.context)

    def test_blog_detail_view_GET(self):
        resp = self.client.get('/blog/testing/')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, template_name='blog/blog_detail.html')
        self.assertTrue('form' in resp.context)
