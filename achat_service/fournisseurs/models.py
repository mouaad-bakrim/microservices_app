from django.db import models

class Fournisseur(models.Model):
    nom = models.CharField(max_length=150, verbose_name="Nom du fournisseur")
    contact = models.CharField(max_length=100, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    actif = models.BooleanField(default=True)

    def __str__(self):
        return self.nom
