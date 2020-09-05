from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, productComment, ProductView
from .forms import ProductCommentForm
from django.views import View
from django.views.generic import DetailView


class All_Products(View):
    template_name = 'products/products.html'

    def get(self, request, *args, **kwargs):
        """ Gives the Login for the Search and the Sort dropdown (Login form Code Institute) """
        products = Product.objects.all()
        query = None
        categories = None
        sort = None
        direction = None
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
                messages.error(
                    request, "Sorry! No Input? Try again Please")
                return redirect(reverse('products:products'))

            search = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(search)

        sorting = f'{sort}_{direction}'

        context = {
            'products': products,
            'search_term': query,
            'current_categories': categories,
            'sorting': sorting,
        }
        return render(request, 'products/products.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def post(self, *args, **kwargs):
        """Adds review to product using the ProductCommentForm and productComment model )"""
        form = ProductCommentForm(self.request.POST)
        if form.is_valid():
            name_product = self.get_object()
            productcomment = form.instance
            rating = form.instance
            productcomment.user = self.request.user
            productcomment.name_product = name_product
            productcomment.save()
            return redirect("products:product_detail", pk=name_product.pk)
        return redirect("products:product_detail", pk=self.get_object().pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form': ProductCommentForm(),
        })
        return context

    def get_object(self):
        """Adds a user views to a product if the user is authenticated, if not returns nothing """
        object = super().get_object()
        if self.request.user.is_authenticated:
            ProductView.objects.get_or_create(
                user=self.request.user, product=object)
        return object
