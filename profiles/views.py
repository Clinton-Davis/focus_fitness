from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, View
from .models import UserProfile
from checkout.models import Order
from blog.models import Blog
from .forms import UserProfileAddressForm
from blog.models import Blog
from memberships.views import (
    get_user_membership,
    get_selected_membership,
    get_user_subscription
)


class ProfileView(LoginRequiredMixin, View):
    template_name = 'profiles/profile.html'
    context_object_name = 'profile'

    def get(self, request, *args, **kwargs):
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


class ProfileSubscription(LoginRequiredMixin, View):
    template = 'profiles/profile_subscriptions.html'
    context_object_name = 'profile'

    def get(self, request, *args, **kwargs):
        profile = get_object_or_404(UserProfile, user=request.user)
        """Displaying user Profile """
        user_membership = get_user_membership(request)
        user_subscription = get_user_subscription(request)
        sub_discout = settings.SUB_DISCOUNT_PERCENTAGE
        context = {
            'profile': profile,
            'user_membership': user_membership,
            'user_subscription': user_subscription,
            'sub_discout': sub_discout
        }

        return render(request, 'profiles/profile_subscriptions.html', context)


@login_required
def shipping_details(request):
    """Displaying User Order history and edit address froms (Login form Code Institute)."""
    template = 'profiles/shipping_details.html'
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileAddressForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your Shipping details have been updated')

    form = UserProfileAddressForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, template, context)


class OrderHistory(LoginRequiredMixin, View):
    template = 'checkout/checkout_success.html'
    context_object_name = 'order'

    def get(self, request, order_number, *args, **kwargs):
        order = get_object_or_404(Order, order_number=order_number)
        messages.info(request, (
            f'This is a past confirmed order: { order_number }.'
        ))
        context = {
            'order': order,
            'from_profile': True,
        }
        return render(request, 'checkout/checkout_success.html', context)


class Cancel_Sub_Confirm(LoginRequiredMixin, TemplateView):
    template_name = "profiles/cancel_sub_confirm.html"
