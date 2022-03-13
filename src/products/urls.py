from django.urls import path

from products.views import ProductViewSet

app_name = "products"

urlpatterns = [
    path(
        r"",
        ProductViewSet.as_view(),
        name="products",
    ),
]
