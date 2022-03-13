from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer
from reservations.serializers import ReservationSerializer


class ProductViewSet(APIView):
    def get(self, request, *args, **kwargs):
        id = request.query_params.get("id", None)

        if id:
            try:
                products = Product.objects.get(id=id)
            except Product.DoesNotExist:
                raise serializers.ValidationError("Product does not exist")

            serializer = ProductSerializer(products)

            return Response(serializer.data, status=status.HTTP_200_OK)

        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        reservation_serializer = ReservationSerializer(data=request.data)

        if not reservation_serializer.is_valid():
            raise serializers.ValidationError(reservation_serializer.errors)

        reservation_serializer.save()

        return Response(status=status.HTTP_201_CREATED)
