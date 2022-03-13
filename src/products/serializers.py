from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    section_name = serializers.CharField(source="section.name", read_only=True)
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "section_name",
            "price",
            "suggested_link",
            "status",
            "image",
            "qr_code",
            "bought",
            "reserved",
            "purchase_limit",
        )
