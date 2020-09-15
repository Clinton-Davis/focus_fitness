from django.urls import path
from . import views
from .views import Cancel_Sub_Confirm


app_name = 'profiles'
urlpatterns = [

    path('', views.profile, name='profile'),
    path('profile_details/', views.ProfileDetail, name='profile_details'),
    path('cancel_sub_confirm/', Cancel_Sub_Confirm.as_view(), name='cancel_sub'),
    path('profile_subscriptions/', views.profile_subscriptions,
         name='profile_subscriptions'),
    path('order_history/<order_number>',
         views.OrderHistory, name='order_history'),
    #     path('<int:pk>/', ShowProfilePageView.as_view(), name='ShowProfilePage')


]
