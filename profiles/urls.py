from django.urls import path
from . import views
from .views import (
    Cancel_Sub_Confirm,
    ShowProfilePageView,
    ProfileView,
    ProfileSubscription,
    OrderHistory
)


app_name = 'profiles'
urlpatterns = [


    path('', ProfileView.as_view(), name='profile'),
    path('shipping_details/', views.shipping_details, name='shipping_details'),
    path('cancel_sub_confirm/', Cancel_Sub_Confirm.as_view(), name='cancel_sub'),
    path('profile_subscriptions/', ProfileSubscription.as_view(),
         name='profile_subscriptions'),
    path('order_history/<order_number>',
         OrderHistory.as_view(), name='order_history'),
    path('userprofile/<int:pk>/',
         ShowProfilePageView.as_view(), name='ShowProfilePage')


]
