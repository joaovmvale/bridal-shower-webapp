from core.storage_backends import PublicMediaStorage
from django.db import models
from django.core.exceptions import ValidationError


class Product(models.Model):
    class StatusChoices(models.IntegerChoices):
        RESERVAR = 1, "Reservar"
        RESERVADO = 2, "Reservado"
        COMPRADO = 3, "Comprado"

    name = models.CharField(
        max_length=255,
        default="",
        verbose_name="Nome do produto",
    )
    section = models.ForeignKey(
        "ProductSection",
        null=True,
        on_delete=models.SET_NULL,
        related_name="products",
        verbose_name="Seção do produto",
    )
    price = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Preço do produto",
    )
    suggested_link = models.URLField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Link sugerido",
    )
    status = models.IntegerField(
        choices=StatusChoices.choices,
        default=StatusChoices.RESERVAR,
        verbose_name="Status do produto",
    )
    image = models.ImageField(
        storage=PublicMediaStorage,
        upload_to="products/images/",
        blank=True,
        default="",
        verbose_name="Imagem do produto",
    )
    qr_code = models.BooleanField(
        default=False,
        verbose_name="Código QR",
    )
    bought = models.PositiveSmallIntegerField(
        default=0,
        verbose_name="Quantidade de compras",
    )
    reserved = models.PositiveSmallIntegerField(
        default=0,
        verbose_name="Quantidade de reservas",
    )
    purchase_limit = models.PositiveSmallIntegerField(
        default=1,
        verbose_name="Limite de compras",
    )

    def clean(self):
        if self.purchase_limit <= 0:
            raise ValidationError("O limite de reservas deve ser maior que zero")

        if self.bought > self.purchase_limit:
            raise ValidationError(
                "O número de compras atuais deve ser menor ou igual ao limite de compras"
            )

        if self.reserved > self.purchase_limit:
            raise ValidationError(
                "O número de reservas atuais deve ser menor ou igual ao limite de reservas"
            )

        if self.status == Product.StatusChoices.RESERVADO:
            if self.reserved < self.purchase_limit:
                raise ValidationError(
                    "O item só pode estar com o status 'RESERVADO' caso a quantidade de reservas seja igual ao limite de compras"
                )

        if self.status == Product.StatusChoices.COMPRADO:
            if self.bought < self.purchase_limit:
                raise ValidationError(
                    "O item só pode estar com o status 'COMPRADO' caso a quantidade de compras seja igual ao limite de compras"
                )

    def save(self, *args, **kwargs):
        self.clean()

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"

    def __str__(self):
        return f"{self.name}"


class ProductSection(models.Model):
    name = models.CharField(
        max_length=100,
        default="",
        verbose_name="Seção do Produto",
        unique=True,
    )

    class Meta:
        verbose_name = "product section"
        verbose_name_plural = "product sections"

    def __str__(self):
        return f"{self.name}"
