from django.contrib import admin
from .models import Produit, CategoryProduit, TVA, Stock, Fournisseur

@admin.register(CategoryProduit)
class CategoryProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description')

@admin.register(TVA)
class TVAAdmin(admin.ModelAdmin):
    list_display = ('nom', 'taux')

@admin.register(Fournisseur)
class FournisseurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'contact', 'telephone', 'actif')
    search_fields = ('nom',)

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type', 'category', 'prix_unitaire', 'tva', 'unite', 'fournisseur', 'actif')
    list_filter = ('type', 'category', 'actif')
    search_fields = ('nom',)

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('produit', 'quantite_disponible', 'seuil_alerte')
