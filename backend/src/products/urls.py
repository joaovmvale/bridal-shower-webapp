from django.urls import path

from products.views import ProductViewSet

app_name = "products"

urlpatterns = [
    path(
        "list/",
        ProductViewSet.as_view(),
        name="products",
    ),
]
