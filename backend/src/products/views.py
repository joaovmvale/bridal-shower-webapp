from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer
from people.models import Person
from reservations.models import Reservation


class ProductViewSet(APIView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        person_name = request.data.get("name")
        person_email = request.data.get("email")
        product_id = request.data.get("product_id")
        reservation_quantity = int(request.data.get("quantity"))
        reservation_status = request.data.get("reservation_status")

        if (
            not person_email
            or not product_id
            or not reservation_quantity
            or not reservation_status
        ):
            return Response(
                "Confira os campos obrigatórios: email, produto, quantidade e status",
                status=status.HTTP_400_BAD_REQUEST,
            )

        person, _ = Person.objects.get_or_create(
            email=person_email,
            defaults={"name": person_name},
        )

        product = Product.objects.get(
            id=product_id,
        )

        if reservation_status == 1:
            product.bought += reservation_quantity
        elif reservation_status == 2:
            product.reserved += reservation_quantity
        product.save()

        Reservation.objects.create(
            product_id=product_id,
            person_id=person.id,
            quantity=reservation_quantity,
            reservation_status=reservation_status,
        )

        return Response(
            status=status.HTTP_201_CREATED,
        )
