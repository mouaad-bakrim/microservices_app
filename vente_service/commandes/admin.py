# from django.contrib import admin
# from .models import CommandeClient, LigneCommande  # utiliser les bons noms de modèles

# class LigneCommandeInline(admin.TabularInline):
#     model = LigneCommande
#     extra = 1

# @admin.register(CommandeClient)
# class CommandeClientAdmin(admin.ModelAdmin):
#     list_display = ('id', 'client', 'date_commande', 'statut', 'total_ht', 'total_ttc', 'total_tva')
#     list_filter = ('statut', 'date_commande')
#     search_fields = ('client__nom',)
#     inlines = [LigneCommandeInline]
