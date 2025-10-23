from django.db import models
from clients.models import Client





class CommandeClient(models.Model):
    """
    Commande passée par un client
    """
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='commandes', verbose_name="Client")
    date_commande = models.DateTimeField(auto_now_add=True, verbose_name="Date de commande")
    statut = models.CharField(
        max_length=20,
        choices=[
            ('brouillon', 'Brouillon'),
            ('validee', 'Validée'),
            ('livree', 'Livrée'),
            ('annulee', 'Annulée'),
        ],
        default='brouillon',
        verbose_name="Statut"
    )

    total_ht = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Total HT")
    total_ttc = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Total TTC")
    total_tva = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Total TVA")
    
    
    class Meta:
        verbose_name = "Commande Client"
        verbose_name_plural = "Commandes Clients"

    def __str__(self):
        return f"Commande #{self.id} - {self.client.nom}"

    def calculer_totaux(self):
        """
        Calcule le total HT et TTC à partir des lignes de commande
        """
        lignes = self.lignes.all()
        total_ht = sum(ligne.prix_total for ligne in lignes)
        self.total_ht = total_ht
        self.total_ttc = total_ht * 1.20  # Exemple : TVA 20%
        self.save()


class LigneCommande(models.Model):
    """
    Les articles (produits) associés à une commande
    """
    commande = models.ForeignKey(
        CommandeClient,
        on_delete=models.CASCADE,
        related_name='lignes',
        verbose_name="Commande"
    )
    produit = models.ForeignKey('vente_service.produits.Produit', on_delete=models.PROTECT)
    quantite = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Quantité")
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix unitaire")
    prix_total = models.DecimalField(max_digits=12, decimal_places=2, editable=False, verbose_name="Prix total")

    class Meta:
        verbose_name = "Ligne de commande"
        verbose_name_plural = "Lignes de commande"

    def __str__(self):
        return f"{self.produit.nom} - {self.quantite} {self.produit.unite}"

    def save(self, *args, **kwargs):
        self.prix_total = self.quantite * self.prix_unitaire
        super().save(*args, **kwargs)
        # Mise à jour automatique du total de la commande
        self.commande.calculer_totaux()
