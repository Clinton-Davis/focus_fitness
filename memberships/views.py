from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from .models import Membership, UserMembership, Subscription

import stripe


def get_user_membership(request):
    """gets the users current membership (Logic and code by Mat @ JustDjango)."""

    user_membership_qs = UserMembership.objects.filter(user=request.user)
    if user_membership_qs.exists():
        return user_membership_qs.first()
    return None


def get_user_subscription(request):
    """Gets the subcription name (Logic and code by Mat @ JustDjango)."""
    user_membership_qs = UserMembership.objects.filter(user=request.user)
    user_subscription_qs = Subscription.objects.filter(
        user_membership=get_user_membership(request))
    if user_subscription_qs.exists():
        user_subscription = user_subscription_qs.first()
        return user_subscription
    return None


def get_selected_membership(request):
    """Gets the membership type from the session (Logic and code by Mat @ JustDjango)."""

    membership_type = request.session['selected_membership_type']
    selected_membership_qs = Membership.objects.filter(
        membership_type=membership_type)
    if selected_membership_qs.exists():
        return selected_membership_qs.first()
    return None


class MembershipSelectView(ListView):

    """List the selected membership (Logic and code by Mat @ JustDjango)."""

    model = Membership
    template_name = 'memberships/membership_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        current_membership = get_user_membership(self.request)
        context['current_membership'] = str(current_membership.membership)
        return context

    def post(self, request, **kwargs):
        selected_membership_type = request.POST.get('membership_type')
        user_membership = get_user_membership(request)
        user_subscription = get_user_subscription(request)
        selected_membership_qs = Membership.objects.filter(
            membership_type=selected_membership_type)
        if selected_membership_qs.exists():
            selected_membership = selected_membership_qs.first()

        """ VALIDATION """

        if user_membership.membership == selected_membership:
            if user_subscription != None:
                messages.info(request, "You have this membership. Your next payment is due \
                    {}".format('get this from stripe'))
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        # assing selected_membership_type to session
        request.session['selected_membership_type'] = selected_membership.membership_type

        return HttpResponseRedirect(reverse('memberships:payment'))


@login_required
def paymentview(request):
    """Provide user with payment form and payment (Logic and code by Mat @ JustDjango)."""

    user_membership = get_user_membership(request)
    try:
        selected_membership = get_selected_membership(request)
    except:
        return redirect(reverse("memberships:select"))

    publicKey = settings.STRIPE_PUBLIC_KEY

    if request.method == "POST":
        try:
            token = request.POST['stripeToken']
            customer = stripe.Customer.retrieve(
                user_membership.stripe_customer_id)
            customer.source = token  # 4242424242424242
            customer.save()
            subscription = stripe.Subscription.create(
                customer=user_membership.stripe_customer_id,
                items=[
                    {
                        "plan": selected_membership.stripe_plan_id,
                    },
                ]
            )
            return redirect(reverse("memberships:update_transactions",
                                    kwargs={'subscription_id': subscription.id}))
        except:
            messages.error(
                request, "An error has occurred, investigate it in the console")
    context = {
        'publicKey': publicKey,
        'selected_membership': selected_membership
    }
    return render(request, 'memberships/membership_payment.html', context)


@login_required
def updatetransaction(request, subscription_id):
    """ Updating the UserMembership model on focus backend (Logic and code by Mat @ JustDjango) """
    user_membership = get_user_membership(request)
    selected_membership = get_selected_membership(request)

    user_membership.membership = selected_membership
    user_membership.save()

    sub, created = Subscription.objects.get_or_create(
        user_membership=user_membership)
    sub.stripe_subscription_id = subscription_id
    sub.active = True
    sub.save()

    try:
        del request.session['selected_membership_type']
    except:
        pass
    messages.success(request, 'Successfully created {} membership'.format(
        selected_membership))
    return redirect('/programs')


@login_required
def cancelsubscription(request):
    """
    Checks to see it user is active, if true retrieves stripe id and deletes it,
    Then sets user active to false, Then turns user membership back to free.
    (Logic and code by Mat @ JustDjango)
    """
    user_sub = get_user_subscription(request)

    if user_sub.active == False:
        messages.info(request, "You dont have a active membership")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    sub = stripe.Subscription.retrieve(user_sub.stripe_subscription_id)
    sub.delete()

    user_sub.active = False
    user_sub.save()

    free_membership = Membership.objects.filter(membership_type='Free').first()
    user_membership = get_user_membership(request)
    user_membership.membership = free_membership
    user_membership.save()

    messages.success(
        request, "Successfully cancelled membership, A email has been sent.")

    return redirect('profiles:profile')
