from django.contrib import admin
from .models import CommandeAchat, LigneCommandeAchat

class LigneCommandeInline(admin.TabularInline):
    model = LigneCommandeAchat
    extra = 1

@admin.register(CommandeAchat)
class CommandeAchatAdmin(admin.ModelAdmin):
    list_display = ('id', 'fournisseur', 'date_commande', 'statut', 'total')
    list_filter = ('statut', 'date_commande')
    search_fields = ('fournisseur__nom',)
    inlines = [LigneCommandeInline]
