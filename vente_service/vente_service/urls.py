
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('commandes/', include('commandes.urls')),
    path('clients/', include('clients.urls')),
]
