from django.urls import path
from .views import (
    MembershipSelectView,
    paymentview,
    updatetransaction,
    cancelsubscription
)


app_name = 'memberships'


urlpatterns = [

    path('', MembershipSelectView.as_view(), name='select_membership'),
    path('payment/', paymentview, name='payment'),
    path('update_transactions/<subscription_id>',
         updatetransaction, name='update_transactions'),
    path('cancel/', cancelsubscription, name='cancel')

]
