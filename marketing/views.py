from django.shortcuts import render

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


def newsletter_subscribe(email):
    """ Sends newletter subscribers email to mailchimps email list """
    data = {
        'email_address': email,
        'status': 'subscribed'
    }

    r = requests.POST(
        members_endpoint,
        auth=("", MAILCHIMP_API_KEY),
        data=json.dumps(data)
    )
    return r.status_code, r.json()


def newletter_signup(request):
    pass
