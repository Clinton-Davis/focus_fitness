from django.urls import path
from . import views
from home.views import AboutView, ContactView, IndexView


urlpatterns = [

    # path('', views.index, name='home'),
    path('', IndexView, name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/',  ContactView.as_view(), name='contact')
]
