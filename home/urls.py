from django.urls import path
from . import views
from home.views import AboutView, ContactView, indexview


urlpatterns = [

    path('', indexview, name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/',  ContactView.as_view(), name='contact')
]
