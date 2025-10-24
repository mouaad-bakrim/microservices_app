# from django.db import models
# from clients.models import Client
# from django.core.exceptions import ValidationError

# class CommandeClient(models.Model):
#     """
#     Représente une commande passée par un client
#     """
#     client = models.ForeignKey(
#         Client,
#         on_delete=models.CASCADE,
#         related_name='commandes',
#         verbose_name="Client"
#     )
#     date_commande = models.DateTimeField(auto_now_add=True, verbose_name="Date de commande")
#     statut = models.CharField(
#         max_length=20,
#         choices=[
#             ('brouillon', 'Brouillon'),
#             ('validee', 'Validée'),
#             ('livree', 'Livrée'),
#             ('annulee', 'Annulée'),
#         ],
#         default='brouillon',
#         verbose_name="Statut"
#     )
#     total_ht = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Total HT")
#     total_ttc = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Total TTC")
#     total_tva = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Total TVA")

#     class Meta:
#         verbose_name = "Commande Client"
#         verbose_name_plural = "Commandes Clients"

#     def __str__(self):
#         return f"Commande #{self.id} - {self.client.nom}"

#     def calculer_totaux(self):
#         """
#         Calcule le total HT, TTC et TVA à partir des lignes de commande
#         """
#         lignes = self.lignes.all()
#         total_ht = sum(ligne.prix_total for ligne in lignes)
#         self.total_ht = total_ht
#         self.total_ttc = total_ht * 1.20  # TVA à 20%
#         self.total_tva = self.total_ttc - total_ht
#         self.save()


# class LigneCommande(models.Model):
#     """
#     Représente une ligne de commande (sans référence à un produit externe)
#     """
#     commande = models.ForeignKey(
#         CommandeClient,
#         on_delete=models.CASCADE,
#         related_name='lignes',
#         verbose_name="Commande"
#     )
#     description = models.CharField(max_length=255, verbose_name="Description du produit")  # Nom ou description
#     quantite = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Quantité")
#     prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix unitaire")
#     prix_total = models.DecimalField(max_digits=12, decimal_places=2, default=0, editable=False, verbose_name="Prix total")
#     date_ligne = models.DateTimeField(auto_now_add=True, verbose_name="Date ligne")

#     class Meta:
#         verbose_name = "Ligne de commande"
#         verbose_name_plural = "Lignes de commande"

#     def __str__(self):
#         return f"{self.description} - {self.quantite} x {self.prix_unitaire}"

#     def clean(self):
#         if self.quantite <= 0:
#             raise ValidationError("La quantité doit être supérieure à zéro")
#         if self.prix_unitaire < 0:
#             raise ValidationError("Le prix unitaire ne peut pas être négatif")

#     def save(self, *args, **kwargs):
#         self.full_clean()  # Valide les champs avant sauvegarde
#         self.prix_total = self.quantite * self.prix_unitaire
#         super().save(*args, **kwargs)
#         self.commande.calculer_totaux()  # Mise à jour automatique du total commande
