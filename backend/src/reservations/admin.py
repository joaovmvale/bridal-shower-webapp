from django.contrib import admin

from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "section",
        "quantity",
        "price",
        "person",
        "email",
    )
    search_fields = (
        "product",
        "section",
        "person",
        "email",
    )
    fieldsets = (
        (
            "Informações da reserva",
            {
                "classes": ("wide",),
                "fields": (
                    "product",
                    "quantity",
                    "person",
                ),
            },
        ),
    )

    @admin.display(description="Preço do produto", ordering="product__price")
    def price(self, obj: Reservation):
        return obj.product.price

    @admin.display(description="Seção do produto", ordering="product__section")
    def section(self, obj: Reservation):
        return obj.product.section

    @admin.display(description="E-mail da pessoa", ordering="person__email")
    def email(self, obj: Reservation):
        return obj.person.email
