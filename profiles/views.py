from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib import messages

from .models import UserProfile
from checkout.models import Order
from .forms import UserProfileAddressForm


def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    """Displaying user Profile """
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
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
