from django.urls import path
from . import views


app_name = 'marketing'

urlpatterns = [

    path('newsubs/', views.newsletter_sub, name='newsubs'),

]
