
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path, include


from home import views

urlpatterns = [
    path('', include('home.urls')),
    path('secret-focus-admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('products/', include('products.urls', namespace='products')),
    path('cart/', include('cart.urls')),
    path('programs/', include('programs.urls', namespace='programs')),
    path('memberships/', include('memberships.urls', namespace='memberships')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('marketing/', include('marketing.urls', namespace='marketing')),
    path('profile/', include('profiles.urls', namespace='profiles')),
    path('checkout/', include('checkout.urls', namespace='checkout')),
    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url('images/favicon.ico')))
]

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)


admin.site.index_title = "Focus Fitness Administration"
admin.site.site_header = "Focus Fitness"
admin.site.site_title = "Focus Fitness"
