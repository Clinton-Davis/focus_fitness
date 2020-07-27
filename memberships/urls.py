from django.urls import path
from .views import MembershipSelectView, paymentview, updatetransaction

app_name = 'memberships'


urlpatterns = [

    path('', MembershipSelectView.as_view(), name='select-membership'),
    path('payment/', paymentview, name='payment'),
    path('update-transactions/<subscription_id>',
         updatetransaction, name='update-transactions')

]
