from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import UserProfile


def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    """Displaying user Prodile """
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)
