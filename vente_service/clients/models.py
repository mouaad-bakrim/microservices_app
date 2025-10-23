from django.db import models


class Category(models.Model):
    """
    Catégorie de client 
    """
    name = models.CharField(max_length=100, unique=True, verbose_name="Nom de la catégorie")
    description = models.TextField(blank=True, null=True, verbose_name="Description")

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"

    def __str__(self):
        return self.name


class Client(models.Model):
    """
    Informations principales du client
    """
    nom = models.CharField(max_length=150, verbose_name="Nom du client")
    adresse = models.CharField(max_length=255, blank=True, null=True, verbose_name="Adresse")
    ville = models.CharField(max_length=100, blank=True, null=True, verbose_name="Ville")
    telephone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Téléphone")
    ice = models.CharField(max_length=30, blank=True, null=True, verbose_name="ICE")
    patente = models.CharField(max_length=30, blank=True, null=True, verbose_name="Patente")
    email = models.EmailField(blank=True, null=True, verbose_name="Email")

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="clients",
        verbose_name="Catégorie"
    )

    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date d’ajout")
    actif = models.BooleanField(default=True, verbose_name="Actif")

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.nom
