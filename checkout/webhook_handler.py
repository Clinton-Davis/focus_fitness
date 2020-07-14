from django.http import HttpResponse


class StripeWH_Handler:

    def __init__(self, request):

        self.request = request

    def handle_event(self, event):
        """ Handles genric/unknow/unexpected events"""

        return HttpResponse(
            content=f'Unhandled Webhook revieved: {event["type"]}',
            status=200
        )

    def handle_event_success(self, event):
        """ Handles payments success intent events"""

        return HttpResponse(
            content=f'Webhook payments revieved: {event["type"]}',
            status=200
        )

    def handle_event_failed(self, event):
        """ Handles payment failing events"""

        return HttpResponse(
            content=f'Webhook failed revieved: {event["type"]}',
            status=200
        )

    def handle_subscription_created(self, event):
        """ Handles subscription creation events"""

        return HttpResponse(
            content=f'Webhook subscription_created revieved: {event["type"]}',
            status=200
        )

    def handle_subscription_deleted(self, event):
        """ Handles  subscription deleting events"""

        return HttpResponse(
            content=f'Webhook subscription deleted revieved: {event["type"]}',
            status=200
        )

    def handle_subscription_updated(self, event):
        """ Handles subscription updating events"""

        return HttpResponse(
            content=f'Webhook subscription updated revieved: {event["type"]}',
            status=200
        )
