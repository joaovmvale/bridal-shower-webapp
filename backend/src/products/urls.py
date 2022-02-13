from django.urls import path

from .views import ProductViewSet

app_name = "products"

urlpatterns = [
    path(
        "products/",
        ProductViewSet.as_view(),
        name="products",
    ),
]
