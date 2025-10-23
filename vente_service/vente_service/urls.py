
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produits/', include('produits.urls')),
    path('commandes/', include('commandes.urls')),
    path('clients/', include('clients.urls')),
]
