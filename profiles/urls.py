from django.urls import path
from . import views


urlpatterns = [

    path('', views.profile, name='profile'),
    path('profile_details/', views.ProfileDetail, name='profile_details'),
    path('profile_subscriptions/', views.profile_subscriptions,
         name='profile_subscriptions'),
    path('order_history/<order_number>',
         views.OrderHistory, name='order_history'),


]
