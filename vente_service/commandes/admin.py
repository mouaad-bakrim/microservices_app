from django.contrib import admin
from .models import CommandeVente, LigneCommandeVente  # tes modèles de commande

class LigneCommandeInline(admin.TabularInline):
    model = LigneCommandeVente
    extra = 1

@admin.register(CommandeVente)
class CommandeVenteAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'date_commande', 'statut', 'total')
    list_filter = ('statut', 'date_commande')
    search_fields = ('client__nom',)
    inlines = [LigneCommandeInline]
