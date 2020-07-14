from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import UserProfile


def profile(request):
    """Displaying user Prodile """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
