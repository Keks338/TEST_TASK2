from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.cashflow_app.urls', namespace='cash')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)