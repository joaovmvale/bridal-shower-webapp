from django.db import models


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
        upload_to="products/images/",
        blank=True,
        default="",
        verbose_name="Imagem do produto",
    )
    qr_code = models.BooleanField(
        default=False,
        verbose_name="Código QR",
    )
    current_reservations = models.PositiveSmallIntegerField(
        default=0,
        verbose_name="Reservas atuais",
    )
    reservation_limit = models.PositiveSmallIntegerField(
        default=1,
        verbose_name="Limite de reservas",
    )

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
