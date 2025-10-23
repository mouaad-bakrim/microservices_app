# Exemple
from django.db import models
from fournisseurs.models import Fournisseur
from vente_service.produits.models import Produit  # Import du produit depuis le service Vente

class CommandeAchat(models.Model):
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    date_commande = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(
        max_length=20,
        choices=[
            ('brouillon', 'Brouillon'),
            ('validee', 'Validée'),
            ('receptionnee', 'Réceptionnée'),
            ('annulee', 'Annulée'),
        ],
        default='brouillon'
    )
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"Commande #{self.id} - {self.fournisseur.nom}"

    def calculer_total(self):
        total = sum([ligne.prix_total for ligne in self.lignes.all()])
        self.total = total
        self.save()


class LigneCommandeAchat(models.Model):
    commande = models.ForeignKey(CommandeAchat, on_delete=models.CASCADE, related_name='lignes')
    quantite = models.DecimalField(max_digits=10, decimal_places=2)
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    prix_total = models.DecimalField(max_digits=12, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.prix_total = self.quantite * self.prix_unitaire
        super().save(*args, **kwargs)
        self.commande.calculer_total()

    def __str__(self):
        return f" {self.quantite} {self.produit.unite}"
