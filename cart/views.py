from django.shortcuts import redirect, reverse, HttpResponse, get_object_or_404
from django.conf import settings
from django.views.generic import TemplateView
from django.contrib import messages
from products.models import Product


class CartView(TemplateView):
    template_name = 'cart/cart.html'

    def get_context_data(self, **kwargs):
        sub_discout = settings.SUB_DISCOUNT_PERCENTAGE
        tax_rate = settings.TAX_RATE_PERCENTAGE
        context = super().get_context_data(**kwargs)
        context['sub_discout'] = sub_discout
        context['tax_rate'] = tax_rate
        context['in_cart'] = True
        return context


def add_to_cart(request, item_id):
    """ Adds a specified product to cart, Checks for sizes and quantity of the sizes
    if sizes are the same it adds to quantity, addes to cart and redirecs to products page
    (Login and Code for Code Institute). Understood and implemented.
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += quantity
                messages.success(request,
                                 (f'Updated size {size.upper()} '
                                  f'{product.name} quantity to '
                                  f'{cart[item_id]["items_by_size"][size]}'))
            else:
                cart[item_id]['items_by_size'][size] = quantity
                messages.success(request,
                                 (f'Added size {size.upper()} '
                                  f'{product.name} to your cart'))
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request,
                             (f'Added size {size.upper()} '
                              f'{product.name} to your cart'))
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(request,
                             (f'Updated {product.name} '
                              f'quantity to {cart[item_id]}'))
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name} to your cart')

    request.session['cart'] = cart

    return redirect(reverse('cart_view'))


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product 
    to the specified amount.
    (Login and Code for Code Institute). Understood and implemented."""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})

    if size:
        if quantity in range(0, 1000):
            cart[item_id]['items_by_size'][size] = quantity
            messages.success(request,
                             (f'{product.name} '
                              f'Updated Size-{size.upper()}'
                              f' Quantity to '
                              f'{cart[item_id]["items_by_size"][size]}'))
        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(request,
                             (f'Removed size {size.upper()} '
                              f'{product.name} from your cart'))
    else:
        if quantity in range(1, 1000):
            cart[item_id] = quantity
            messages.success(request,
                             (f'Updated {product.name} '
                              f'quantity to {cart[item_id]}'))
        else:
            cart.pop(item_id)
            messages.success(request,
                             (f'Removed {product.name} '
                              f'from your cart'))

    request.session['cart'] = cart
    return redirect(reverse('cart_view'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart
    (Login and Code for Code Institute). Understood and implemented."""
    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        cart = request.session.get('cart', {})

        if size:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(
                request, f'Removed Size {size.upper()} {product.name}')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name}')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error Removing Item: {e}')
        return HttpResponse(status=500)
