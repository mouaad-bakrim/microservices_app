# from django.db import models



# class CategoryProduit(models.Model):
#     """
#     Catégorie des produits
#     """
#     nom = models.CharField(max_length=100, unique=True, verbose_name="Nom de la catégorie")
#     description = models.TextField(blank=True, null=True, verbose_name="Description")

#     class Meta:
#         verbose_name = "Catégorie de produit"
#         verbose_name_plural = "Catégories de produit"

#     def __str__(self):
#         return self.nom


# class TVA(models.Model):
#     """
#     Taux de TVA applicable
#     """
#     nom = models.CharField(max_length=50, unique=True, verbose_name="Nom TVA")
#     taux = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Taux (%)")  # Ex: 20.00

#     class Meta:
#         verbose_name = "TVA"
#         verbose_name_plural = "TVA"

#     def __str__(self):
#         return f"{self.nom} ({self.taux}%)"


# class Produit(models.Model):
#     """
#     Les produits vendus ou stockés dans le service Vente
#     """
#     TYPE_CHOICES = [
#         ('carburant', 'Carburant'),
#         ('lubrifiant', 'Lubrifiant'),
#         ('autre', 'Autre'),
#     ]

#     nom = models.CharField(max_length=100, unique=True, verbose_name="Nom du produit")
#     type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='autre', verbose_name="Type de produit")
#     category = models.ForeignKey(
#         CategoryProduit,
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         related_name="produits",
#         verbose_name="Catégorie"
#     )
#     prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix unitaire")
#     tva = models.ForeignKey(
#         TVA,
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#         related_name="produits",
#         verbose_name="TVA"
#     )
#     unite = models.CharField(max_length=10, default='L', verbose_name="Unité de mesure")

#     actif = models.BooleanField(default=True, verbose_name="Actif")
#     date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date d’ajout")

#     class Meta:
#         verbose_name = "Produit"
#         verbose_name_plural = "Produits"

#     def __str__(self):
#         return f"{self.nom} ({self.unite})"

