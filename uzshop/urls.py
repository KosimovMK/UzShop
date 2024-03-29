from django.contrib import admin
from django.urls import path, include
from catalog.views import inedx
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inedx, name='index'),
    path('catalog/', include('catalog.urls', namespace='catalog')),
    path('users/', include('users.urls', namespace='users')),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
