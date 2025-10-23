from django.db import models


class Fournisseur(models.Model):
    """
    Fournisseur des produits
    """
    nom = models.CharField(max_length=150, verbose_name="Nom du fournisseur")
    contact = models.CharField(max_length=100, blank=True, null=True, verbose_name="Contact")
    telephone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Téléphone")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")
    adresse = models.CharField(max_length=255, blank=True, null=True, verbose_name="Adresse")
    actif = models.BooleanField(default=True, verbose_name="Actif")

    class Meta:
        verbose_name = "Fournisseur"
        verbose_name_plural = "Fournisseurs"

    def __str__(self):
        return self.nom
        
class CategoryProduit(models.Model):
    """
    Catégorie des produits
    """
    nom = models.CharField(max_length=100, unique=True, verbose_name="Nom de la catégorie")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    class Meta:
        verbose_name = "Catégorie de produit"
        verbose_name_plural = "Catégories de produit"

    def __str__(self):
        return self.nom


class TVA(models.Model):
    """
    Taux de TVA applicable
    """
    nom = models.CharField(max_length=50, unique=True, verbose_name="Nom TVA")
    taux = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Taux (%)")  # Ex: 20.00

    class Meta:
        verbose_name = "TVA"
        verbose_name_plural = "TVA"

    def __str__(self):
        return f"{self.nom} ({self.taux}%)"


class Produit(models.Model):
    """
    Les produits vendus ou stockés dans le service Vente
    """
    TYPE_CHOICES = [
        ('carburant', 'Carburant'),
        ('lubrifiant', 'Lubrifiant'),
        ('autre', 'Autre'),
    ]

    nom = models.CharField(max_length=100, unique=True, verbose_name="Nom du produit")
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='autre', verbose_name="Type de produit")
    category = models.ForeignKey(
        CategoryProduit,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="produits",
        verbose_name="Catégorie"
    )
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix unitaire")
    tva = models.ForeignKey(
        TVA,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="produits",
        verbose_name="TVA"
    )
    unite = models.CharField(max_length=10, default='L', verbose_name="Unité de mesure")
    fournisseur = models.ForeignKey(
        'Fournisseur', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Fournisseur"
    )
    actif = models.BooleanField(default=True, verbose_name="Actif")
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date d’ajout")

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"

    def __str__(self):
        return f"{self.nom} ({self.unite})"



class Stock(models.Model):
    """
    Gestion du stock des produits
    """
    produit = models.OneToOneField(Produit, on_delete=models.CASCADE, related_name='stock', verbose_name="Produit")
    quantite_disponible = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="Quantité disponible")
    seuil_alerte = models.DecimalField(max_digits=12, decimal_places=2, default=10, verbose_name="Seuil d’alerte")  # notification stock bas

    class Meta:
        verbose_name = "Stock"
        verbose_name_plural = "Stocks"

    def __str__(self):
        return f"{self.produit.nom} - {self.quantite_disponible} {self.produit.unite}"

    def retirer_quantite(self, quantite):
        """
        Retire une quantité du stock
        """
        if quantite > self.quantite_disponible:
            raise ValueError("Stock insuffisant")
        self.quantite_disponible -= quantite
        self.save()

    def ajouter_quantite(self, quantite):
        """
        Ajoute une quantité au stock
        """
        self.quantite_disponible += quantite
        self.save()
