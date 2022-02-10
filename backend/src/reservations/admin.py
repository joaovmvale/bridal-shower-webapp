from django.contrib import admin

from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    # Campos que serão listados
    list_display = (
        "product",
        "person",
    )
    search_fields = (
        "product",
        "person",
    )
    fieldsets = (
        (
            "Informações da reserva",
            {
                "classes": ("wide",),
                "fields": (
                    "product",
                    "person",
                ),
            },
        ),
    )
