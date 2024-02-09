from catalog.views import catalog
from django.urls import path, include

app_name = 'catalog'

urlpatterns = [
    path('', catalog, name='index')
]
