from django.urls import path
from .views import (
    MembershipSelectView,
    paymentview,
    updatetransaction,
    cancelsubscription
)


app_name = 'memberships'


urlpatterns = [

    path('', MembershipSelectView.as_view(), name='select-membership'),
    path('payment/', paymentview, name='payment'),
    path('update-transactions/<subscription_id>',
         updatetransaction, name='update-transactions'),
    path('cancel/', cancelsubscription, name='cancel')

]
