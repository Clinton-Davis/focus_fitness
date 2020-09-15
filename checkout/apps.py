from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'
    verbose_name = "Product Orders"

    def ready(self):
        import checkout.signals
