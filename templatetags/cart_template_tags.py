from django import template
from cart.utils import get_or_set_order_session


register = template.Library()


@register.filter
def cart_total(request):
    order = get_or_set_order_session(request)
    cart_total = order.get_total()
    return cart_total
