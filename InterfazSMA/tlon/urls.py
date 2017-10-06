from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static

from django.conf.urls import handler404
from apps.inicio.views import error_404
 
handler404 = error_404

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.inicio.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 