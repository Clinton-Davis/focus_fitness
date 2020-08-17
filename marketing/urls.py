from django.urls import path
from . import views
from .views import newsletter_sub

app_name = 'marketing'

urlpatterns = [

    path('newsubs/', views.newsletter_sub, name='newsubs'),

]
