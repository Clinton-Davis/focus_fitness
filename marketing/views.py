from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib import messages
from .forms import NewLetterEmailSignupForm
from .models import NewsLetterSignups

# Create your views here.
import requests
import json


MAILCHIMP_EMAIL_LIST_ID = settings.MAILCHIMP_EMAIL_LIST_ID
MAILCHIMP_DATA_CENTER = settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY

api_url = 'https://{dc}.api.mailchimp.com/3.0'.format(dc=MAILCHIMP_DATA_CENTER)
members_endpoint = '{api_url}/lists/{list_id}/members'.format(
    api_url=api_url,
    list_id=MAILCHIMP_EMAIL_LIST_ID
)


def newsletter_sub(request):
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


# def newsletter_subscribe(email):
#     """ Sends newletter subscribers email to mailchimps email list """
#     data = {
#         'email_address': email,
#         'status': 'subscribed'
#     }
#     r = requests.POST(
#         members_endpoint,
#         auth=("", MAILCHIMP_API_KEY),
#         data=json.dumps(data)
#     )
#     print(data)
#     return r.status_code, r.json()


# def newsletter_signup(request):
#     """Check to see if form is post, checks to see if user 
#         has already joined if True message else save email
#         and send email instance to newsletter_subcrible function"""
#     form = NewLetterEmailSignupForm(request.POST or None)
#     if request.method == 'POST':
#         if form.is_valid():
#             newslettersignups_qs = NewsLetterSignups.objects.filter(
#                 email=form.instance.email)
#             if newslettersignups_qs.exists():
#                 messages.info(
#                     request, 'You are already part of the News Letter mailing list')
#             else:
#                 newsletter_subscribe(form.instance.email)
#                 form.save()
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
