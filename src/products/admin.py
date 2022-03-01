from django.contrib import admin

from .models import Product, ProductSection


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "section",
        "price",
        "suggested_link",
        "status",
        "reserved",
        "bought",
        "purchase_limit",
    )
    list_filter = (
        "status",
        "section",
    )
    search_fields = ("name",)
    ordering = (
        "reserved",
        "bought",
        "purchase_limit",
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
                    "reserved",
                    "bought",
                    "purchase_limit",
                ),
            },
        ),
    )


@admin.register(ProductSection)
class ProductSectionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ("name",)
    fieldsets = (
        (
            "Informações da seção",
            {
                "classes": ("wide",),
                "fields": ("name",),
            },
        ),
    )
