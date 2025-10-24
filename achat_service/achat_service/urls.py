from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('commandes/', include('commandes.urls')),
    path('fournisseurs/', include('fournisseurs.urls')),

    # rediriger la racine vers /commandes/ ou une page d’accueil
    path('', lambda request: HttpResponseRedirect('/commandes/')),
]
