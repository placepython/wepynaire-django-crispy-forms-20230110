from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Exemple d'utilisateur."""

    first_name = None
    last_name = None
    name = models.CharField(max_length=255, blank=True)
    addresses = models.ManyToManyField(
        "Address",
        related_name="users",
        through="UserAddress",
    )


class UserAddress(models.Model):
    """Modèle de liaison entre utilisateur et adresse."""

    class AdresseRoles(models.TextChoices):
        HOME = "home", "Adresse de domicile"
        INVOICE = "invoice", "Adresse de facturation"
        DELIVERY = "delivery", "Adresse de livraison principale"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    address = models.ForeignKey("Address", on_delete=models.CASCADE)
    address_role = models.CharField(
        "role de l'adresse",
        max_length=255,
        choices=AdresseRoles.choices,
        default=AdresseRoles.HOME,
    )
    created = models.DateTimeField("date de création", auto_now_add=True)
    updated = models.DateTimeField("date de mise à jour", auto_now=True)


class Address(models.Model):
    """Représente une adresse postale."""

    class Countries(models.TextChoices):
        SWITZERLAND = "CH", "Suisse"
        FRANCE = "F", "France"
        BELGIUM = "B", "Belgique"
        CANADA = "CAN", "Canada"

    street = models.CharField("rue", max_length=255, blank=True)
    street_number = models.CharField(
        "numéro de la rue", max_length=6, blank=True
    )
    address_complement = models.CharField(
        "complément d'adresse", max_length=255, blank=True
    )
    city = models.CharField("ville", max_length=100)
    zip_code = models.CharField("numéro postal", max_length=6)
    country = models.CharField(
        "pays",
        max_length=4,
        choices=Countries.choices,
        default=Countries.SWITZERLAND,
    )
