from django.db import models

from people.models import Person
from products.models import Product


class Reservation(models.Model):
    class ReservationStatus(models.IntegerChoices):
        CONFIRMED = 1, "Confirmado"
        THINKING = 2, "Pensando"

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
    quantity = models.PositiveSmallIntegerField(
        default=0,
        verbose_name="Quantidade reservada",
    )
    reservation_status = models.IntegerField(
        choices=ReservationStatus.choices,
        blank=False,
        null=False,
        verbose_name="Status da reserva",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data da reserva",
    )

    class Meta:
        verbose_name = "reservation"
        verbose_name_plural = "reservations"

    def __str__(self):
        return f"{self.product} - {self.person}"
