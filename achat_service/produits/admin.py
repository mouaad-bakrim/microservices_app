from django.contrib import admin
from .models import Produit

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix_achat', 'unite', 'fournisseur', 'actif')
    search_fields = ('nom',)
    list_filter = ('actif',)
