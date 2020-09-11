from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import UserProfile
from checkout.models import Order
from .forms import UserProfileAddressForm
from blog.models import Blog
from memberships.views import (
    get_user_membership,
    get_selected_membership,
    get_user_subscription
)


@login_required
def profile(request):
    template_name = 'profiles/profile.html'

    profile = get_object_or_404(UserProfile, user=request.user)
    """Displaying user Profile """
    user_membership = get_user_membership(request)
    user_subscription = get_user_subscription(request)
    orders = profile.Orders.all().order_by('-date')
    user_blog = Blog.objects.filter(
        author=request.user).order_by('-publish_date')

    context = {
        'profile': profile,
        'user_membership': user_membership,
        'user_subscription': user_subscription,
        'orders': orders,
        'user_blog': user_blog,
    }

    return render(request, 'profiles/profile.html', context)


@login_required
def profile_subscriptions(request):
    template = 'profiles/profile_subscriptions.html'
    profile = get_object_or_404(UserProfile, user=request.user)
    """Displaying user Profile """
    user_membership = get_user_membership(request)
    user_subscription = get_user_subscription(request)

    context = {
        'profile': profile,
        'user_membership': user_membership,
        'user_subscription': user_subscription
    }

    return render(request, template, context)


@login_required
def ProfileDetail(request):
    """Displaying User Order history and edit address froms (Login form Code Institute)"""
    template = 'profiles/profile_details.html'
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileAddressForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your Shipping details have been updated')

    form = UserProfileAddressForm(instance=profile)
    orders = profile.Orders.all()

    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


@login_required
def OrderHistory(request, order_number):
    """
    Gets a past oder and displays if with a message
    (Login and Code form Code Institute)
    """
    template = 'checkout/checkout_success.html'
    order = get_object_or_404(Order, order_number=order_number)
    messages.info(request, (
        f'This is a past confirmed order: { order_number }.'
    ))
    context = {
        'order': order,
        'from_profile': True,
    }
    return render(request, template, context)


class Cancel_Sub_Confirm(LoginRequiredMixin, TemplateView):
    template_name = "profiles/cancel_sub_confirm.html"
