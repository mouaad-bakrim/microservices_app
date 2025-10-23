from django.contrib import admin
from .models import Fournisseur

@admin.register(Fournisseur)
class FournisseurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'contact', 'telephone', 'email', 'actif')
    search_fields = ('nom', 'contact', 'telephone')
    list_filter = ('actif',)
