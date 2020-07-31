from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib import messages

from .models import UserProfile
from checkout.models import Order
from .forms import UserProfileAddressForm
from blog.models import Blog
from memberships.views import (
    get_user_membership,
    get_selected_membership,
    get_user_subscription
)


def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    """Displaying user Profile """
    user_membership = get_user_membership(request)
    user_subscription = get_user_subscription(request)
    orders = profile.Orders.all()
    user_blog = Blog.objects.filter(author=request.user)

    template = 'profiles/profile.html'
    context = {
        'profile': profile,
        'user_membership': user_membership,
        'user_subscription': user_subscription,
        'orders': orders,
        'user_blog': user_blog,
    }

    return render(request, template, context)


def profile_subscriptions(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    """Displaying user Profile """
    user_membership = get_user_membership(request)
    user_subscription = get_user_subscription(request)

    template = 'profiles/profile_subscriptions.html'
    context = {
        'profile': profile,
        'user_membership': user_membership,
        'user_subscription': user_subscription
    }

    return render(request, template, context)


def ProfileDetail(request):
    """Displaying User Order history and edit address froms """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileAddressForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your Shipping details have been updated')
    # This line below populates forms with instance of profile saved details
    form = UserProfileAddressForm(instance=profile)
    orders = profile.Orders.all()

    template = 'profiles/profile_details.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


def OrderHistory(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmed order: { order_number }.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
