from django.shortcuts import render


def CarView(request):
    """A view to the cart contents page """

    return render(request, 'cart/cart.html')
