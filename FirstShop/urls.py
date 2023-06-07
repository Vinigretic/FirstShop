from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('orders/', include('orders.urls', namespace='orders')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('discount/', include('discount.urls', namespace='discount')),
    path('rosetta/', include('rosetta.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
)

urlpatterns += i18n_patterns(
    path('', include('shop.urls', namespace='shop')),
)


if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
