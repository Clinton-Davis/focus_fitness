from django.urls import path
from . import views


urlpatterns = [

    path('', views.CarView, name='CarView'),

]
