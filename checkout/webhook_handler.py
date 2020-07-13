from django.http import HttpResponse


class StripeWH_Handler:

    def __init__(self, request):

        self.request = request

    def handle_event(self, event):
        """ Handles genric/unknow/unexpected events"""

        return HttpResponse(
            content=f'Webhook revieved: {event["type"]}',
            status=200
        )
