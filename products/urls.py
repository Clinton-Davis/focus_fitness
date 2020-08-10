from django.urls import path
from . import views
from .views import ProductDetailView

app_name = 'products'
urlpatterns = [

    path('', views.all_products, name='products'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

]
