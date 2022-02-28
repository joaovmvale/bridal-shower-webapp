from rest_framework import serializers
from people.models import Person

from products.models import Product

from .models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=255,
        default="",
        source="person.name",
    )
    email = serializers.EmailField(
        source="person.email",
    )
    product = serializers.IntegerField()
    quantity = serializers.IntegerField()
    reservation_status = serializers.IntegerField()

    class Meta:
        model = Reservation
        fields = [
            "name",
            "email",
            "product",
            "quantity",
            "reservation_status",
        ]

    def validate_product(self, value):
        try:
            return Product.objects.get(id=value).pk
        except Product.DoesNotExist:
            raise serializers.ValidationError("Produto não encontrado")

    def validate_reservation_status(self, value):
        try:
            return Reservation.ReservationStatus(value).value
        except (ValueError, KeyError):
            raise serializers.ValidationError("Status inválido")

    def validate(self, data):
        if (
            not data["person"]["name"]
            or not data["person"]["email"]
            or not data["product"]
            or not data["quantity"]
            or not data["reservation_status"]
        ):
            raise serializers.ValidationError(
                "Confira os campos obrigatórios: nome, email, produto, quantidade e status"
            )

        return data

    def create(self, validated_data):
        person, _ = Person.objects.get_or_create(
            email=validated_data["person"]["email"],
            defaults={
                "name": validated_data["person"]["name"],
            },
        )

        product = Product.objects.get(
            id=validated_data["product"],
        )

        if (
            validated_data["reservation_status"]
            == Reservation.ReservationStatus.CONFIRMED
        ):
            product.bought += validated_data["quantity"]
        elif (
            validated_data["reservation_status"]
            == Reservation.ReservationStatus.THINKING
        ):
            product.reserved += validated_data["quantity"]
        product.save()

        reservation, created = Reservation.objects.get_or_create(
            person_id=person.id,
            product_id=product.id,
            reservation_status=validated_data["reservation_status"],
            defaults={
                "quantity": validated_data["quantity"],
            },
        )

        if not created:
            reservation.quantity += validated_data["quantity"]
            reservation.save()
            return reservation

        return reservation
