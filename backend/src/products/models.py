from email.policy import default
from django.db import models
from django.core.exceptions import ValidationError


class Product(models.Model):
    class LabelChoices(models.IntegerChoices):
        RESERVAR = 1, "Reservar"
        RESERVADO = 2, "Reservado"
        COMPRADO = 3, "Comprado"

    name = models.CharField(
        max_length=255,
        default="",
    )
    section = models.CharField(
        max_length=100,
        default="",
    )
    price = models.FloatField(
        null=True,
        blank=True,
    )
    suggested_link = models.URLField(
        max_length=255,
        null=True,
        blank=True,
    )
    label = models.IntegerField(
        choices=LabelChoices.choices,
        default=LabelChoices.RESERVAR,
    )
    image = models.ImageField(
        upload_to="products/images/",
        default="",
    )
    qr_code = models.BooleanField(
        default=False,
    )
    reservation_limit = models.PositiveSmallIntegerField(
        default=0,
    )
    reserved_by = models.ForeignKey(
        "Person",
        on_delete=models.SET_NULL,
        related_name="reserved_products",
        default=None,
    )

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):
    name = models.CharField(
        max_length=255,
        default="",
    )
    email = models.EmailField(
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "person"
        verbose_name_plural = "people"

    def __str__(self):
        return f"{self.name}"
