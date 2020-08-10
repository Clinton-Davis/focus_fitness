from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from django.views.generic import DetailView


def all_products(request):
    """A view to show all products, including sorting and searching"""
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Sorry! No Input? Try again Please")
                return redirect(reverse('products'))

            search = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(search)

    sorting = f'{sort}_{direction}'

    template_name = 'products/products.html'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'sorting': sorting,


    }

    return render(request, 'products/products.html', context)


# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'products/product_detail.html'

def product_detail(request, product_id):
    """A view to show product details, """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
