
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path, include


from home import views

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('products/', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('programs/', include('programs.urls', namespace='programs')),
    path('memberships/', include('memberships.urls', namespace='memberships')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('marketing/', include('marketing.urls', namespace='marketing')),
    path('profile/', include('profiles.urls')),
    path('checkout/', include('checkout.urls')),
    # path('newsignups/', newsletter_sub, name='newsletter_sub'),

    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url('images/favicon.ico')))
]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
