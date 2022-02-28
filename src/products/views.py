from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer
from people.models import Person
from reservations.models import Reservation
from reservations.serializers import ReservationSerializer


class ProductViewSet(APIView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        reservation_serializer = ReservationSerializer(data=request.data)

        if not reservation_serializer.is_valid():
            raise serializers.ValidationError(reservation_serializer.errors)

        reservation_serializer.save()

        return Response(status=status.HTTP_201_CREATED)
