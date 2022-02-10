from django.contrib import admin

from .models import Product, ProductSection


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Campos que serão listados
    list_display = (
        "name",
        "section",
        "price",
        "suggested_link",
        "status",
        "current_reservations",
        "reservation_limit",
    )
    list_filter = (
        "status",
        "section",
    )
    search_fields = ("name",)
    ordering = (
        "current_reservations",
        "reservation_limit",
    )
    fieldsets = (
        (
            "Informações do produto",
            {
                "classes": ("wide",),
                "fields": (
                    "name",
                    "section",
                    "price",
                    "suggested_link",
                    "status",
                    "image",
                    "qr_code",
                    "current_reservations",
                    "reservation_limit",
                ),
            },
        ),
    )
