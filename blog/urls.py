from django.urls import path
from . import views
from blog.views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    like,
)

app_name = 'blog'

urlpatterns = [

    path('', BlogListView.as_view(), name='list'),
    path('create/',  BlogCreateView.as_view(), name='create'),
    path('<slug>/', BlogDetailView.as_view(), name='details'),
    path('<slug>/update/', BlogUpdateView.as_view(), name='update'),
    path('<slug>/delete',  BlogDeleteView.as_view(), name='delete'),
    path('like/<slug>/',  like, name='like')
]
