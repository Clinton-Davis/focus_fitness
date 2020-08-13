from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category,  productComment
from .forms import ProductCommentForm
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


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_details.html'
    context_object_name = 'product'

    # def post(self, *args, **kwargs):
    #     """ name_product is the product (pk)"""
    #     form = ProductCommentForm(self.request.POST)
    #     if form.is_valid():
    #         name_product = self.get_object()
    #         comment = form.instance
    #         comment.user = self.request.user
    #         comment.name_product = name_product
    #         comment.save()
    #         return redirect("product_detail", pk=name_product.pk)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = ProductCommentForm()
    #     return context

    # def get_object(self, **kwargs):

    #     object = super().get_object(**kwargs)
    #     if self.request.user.is_authenticated:
    #         productComment.objects.get_or_create(
    #             user=self.request.user, name_product=object)
    #     return object


# def product_detail(request, pk):
#     """A view to show product details, """
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         'product': product,
#     }
#     return render(request, 'products/product_detail.html', context)
