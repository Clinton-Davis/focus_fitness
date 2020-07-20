from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog, BlogComment, BlogView, Like
from .forms import BlogPostForm


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog


class BlogCreateView(CreateView):
    form_class = BlogPostForm
    model = Blog
    success_url = '/blog/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'create'
        })
        return context


class BlogUpdateView(UpdateView):
    form_class = BlogPostForm
    model = Blog
    success_url = '/blog/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'update'
        })
        return context


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = '/blog/'
