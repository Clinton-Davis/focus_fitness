from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.views.generic import TemplateView
from django.contrib import messages
from products.models import Product


class CartView(TemplateView):
    template_name = 'cart/cart.html'


def add_to_cart(request, item_id):
    """ Adds a specified product to cart, Checks for sizes and quantity of the sizes
    if sizes are the same it adds to quantity, addes to cart and redirecs to products page
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
                messages.success(
                    request, f'Updated size {size.upper()} - {product.name}')
            else:
                cart[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request, f'Added size {size.upper()} - {product.name}')
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request, f'Added size {size.upper()} - {product.name}')

    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(
                request, f'Updated {product.name}')
        else:
            cart[item_id] = quantity
            messages.success(request, f'Added {product.name}')

    request.session['cart'] = cart
    return redirect(reverse('products:products'))


def adjust_cart(request, item_id):
    """ Adjust the quantity of the specified product to the specified amount """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    cart = request.session.get('cart', {})
    if size:
        if quantity > 0:
            cart[item_id]['items_by_size'][size] = quantity
            messages.success(
                request, f'Updated size {size.upper()} - {product.name}')
        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.warning(
                request, f'Removed size {size.upper()} - {product.name}')
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(
                request, f'Updated {product.name}')
        else:
            cart.pop[item_id]
            messages.warning(request, f'Removed {product.name}')
    request.session['cart'] = cart
    return redirect(reverse('cart_view'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""
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
            messages.warning(
                request, f'Removed size {size.upper()} {product.name}')
        else:
            cart.pop(item_id)
            messages.warning(request, f'Removed {product.name}')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
