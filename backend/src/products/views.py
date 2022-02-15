from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer


class ProductViewSet(APIView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Dados a receber:
        * User:
        - name
        - email

        * Reservation:
        - quantity
        """
        user_data = {
            "name": request.data.get("name"),
            "email": request.data.get("email"),
        }

        reservation_data = {
            "product_id": request.data.get("product_id"),
            "quantity": request.data.get("quantity"),
        }
