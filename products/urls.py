from django.urls import path
from . import views
from products.views import DetailView
from products.views import ProductDetailView


urlpatterns = [

    path('', views.all_products, name='products'),
    # path('<pk>/', views.product_detail, name='product_detail'),
    path('<pk>/', ProductDetailView.as_view(), name='product_detail'),

]
