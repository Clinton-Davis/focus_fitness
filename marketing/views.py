from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib import messages
from .forms import NewLetterEmailSignupForm
from .models import NewsLetterSignups


def newsletter_sub(request):
    """Gets the emails from form, Checks to see it the email
        is in the db, if it is sends a message and if its not
        It saves the email. 
    """
    form = NewLetterEmailSignupForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            newslettersignups_qs = NewsLetterSignups.objects.filter(
                email=form.instance.email)
            if newslettersignups_qs.exists():
                messages.info(
                    request, 'You are already part of the News Letter mailing list')
            else:
                email = request.POST["email"]
                new_signup = NewsLetterSignups()
                new_signup.email = email
                new_signup.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
