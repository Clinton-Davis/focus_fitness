from django.urls import path
from . import views
from blog.views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    like,
    CategoryView,

)

app_name = 'blog'

urlpatterns = [

    # path('', BlogListView.as_view(), name='list'),
    path('', BlogListView, name='list'),
    path('create/',  BlogCreateView.as_view(), name='create'),
    path('<slug>/', BlogDetailView.as_view(), name='details'),
    path('<slug>/update/', BlogUpdateView.as_view(), name='update'),
    path('<slug>/delete/',  BlogDeleteView.as_view(), name='delete'),
    path('category/<str:category>/',  CategoryView, name='category'),
    path('like/<slug>/',  like, name='like')
]
