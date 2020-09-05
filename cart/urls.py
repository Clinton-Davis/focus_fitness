from django.urls import path
from . import views
from cart.views import CartView


urlpatterns = [

    path('', CartView.as_view(), name='cart_view'),
    path('add/<item_id>/', views.add_to_cart, name='add_to_cart'),
    # path('adjust/<item_id>/', views.adjust_cart, name='adjust_cart'),
    path('remove/<item_id>/', views.remove_from_cart, name='remove_from_cart'),

]
