from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from memberships.views import get_user_membership
from marketing.models import NewsLetterSignups
from marketing.forms import NewLetterEmailSignupForm
from django_user_agents.utils import get_user_agent


def from_settings(request):
    """This Keeps the admin 'ENVIRONMENT_NAME' in the golbal context"""
    return {
        "ENVIRONMENT_NAME":  settings.ENVIRONMENT_NAME,
    }


def get_screen_size(request):
    """Checks to see if user is on moble or not"""
    user_agent = get_user_agent(request)
    if user_agent.is_mobile:
        screen_size = True
    else:
        screen_size = False
    return screen_size


def get_loged_user_discount(request):
    """Checks to see if the use is authenticated.
        Looks to get_user_membership function in memberships.views for current membership.
        If membership is 'Pro' added discount to cart"""
    if request.user.is_authenticated:
        current_membership = get_user_membership(request)
        current_membership = str(current_membership.membership)
    else:
        current_membership = False

    if current_membership == "Professional":
        discount = True
        return discount
    else:
        return None


def global_context(request):
    """ Makes the global_context context avaible to all apps.
        create a seession var called cart
        adds the items to cart with with all product data
        calls the 'get_loged_user_discount' fuction to check the user membership static
        does a the maths with delivery charges/ Tax amount/ and discounts if applicable
        Calls the 'get_screen_size' fuction to get screen size and adds into global context
        (Cart Login from Code Institute adapted to work for Focus)
    """
    cart_items = []
    total = 0
    product_count = 0
    discount = 0
    tax = 0
    form = NewLetterEmailSignupForm()
    cart = request.session.get('cart', {})
    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })
    if request.user.is_authenticated:
        user_discount = get_loged_user_discount(request)
        if user_discount == True:
            discount = total * Decimal(settings.SUB_DISCOUNT_PERCENTAGE / 100)
    else:
        discount = 0
    screen_size = get_screen_size(request)
    cart_total = total
    sub_total = cart_total - discount
    delivery = sub_total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    tax = sub_total * Decimal(settings.TAX_RATE_PERCENTAGE / 100)
    grand_total = sub_total + delivery
    tax_rate = Decimal(settings.TAX_RATE_PERCENTAGE)
    discount_percentage = Decimal(settings.SUB_DISCOUNT_PERCENTAGE)
    context = {
        'cart_items': cart_items,
        'sub_total': sub_total,
        'tax': tax,
        'cart_total': cart_total,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'discount': discount,
        'grand_total': grand_total,
        'news_form': form,
        'screen_size': screen_size
    }
    return context
