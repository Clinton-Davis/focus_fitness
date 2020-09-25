from django.urls import path
from products.views import ProductDetailView, All_Products

app_name = 'products'

urlpatterns = [

    path('', All_Products.as_view(), name='products'),
    path('<pk>/', ProductDetailView.as_view(), name='product_detail'),

]
