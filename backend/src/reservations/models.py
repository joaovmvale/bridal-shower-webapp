from django.db import models

from people.models import Person
from products.models import Product


class Reservation(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="reservations",
        verbose_name="Produto reservado",
    )
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="reservations",
        verbose_name="Reservado por",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data de criação",
    )

    class Meta:
        verbose_name = "reservation"
        verbose_name_plural = "reservations"

    def __str__(self):
        return f"{self.product} - {self.person}"
