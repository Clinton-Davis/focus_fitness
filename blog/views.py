from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Blog, BlogComment, BlogView, Like
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = (
        'title',
        'content',
        'thumbnail',
        'author',
        'slug',
    )


class BlogUpdateView(UpdateView):
    model = Blog
    fields = (
        'title',
        'content',
        'thumbnail',
        'author',
        'slug',
    )


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = '/blog/'
