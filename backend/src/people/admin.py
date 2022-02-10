from django.contrib import admin

from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    # Campos que serão listados
    list_display = (
        "name",
        "email",
    )
    search_fields = (
        "name",
        "email",
    )
    ordering = (
        "name",
        "email",
    )
    fieldsets = (
        (
            "Informações da pessoa",
            {
                "classes": ("wide",),
                "fields": (
                    "name",
                    "email",
                ),
            },
        ),
    )
