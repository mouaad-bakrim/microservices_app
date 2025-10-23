from django.contrib import admin
from .models import Client, CategoryClient  # si tu as un modèle CategoryClient

@admin.register(CategoryClient)
class CategoryClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom', 'categorie', 'adresse', 'ville', 'telephone', 'email')
    search_fields = ('nom', 'ville', 'telephone')
    list_filter = ('categorie',)
