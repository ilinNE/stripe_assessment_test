from django.urls import path

from .views import (
    BuyItemAPIView,
    GetItemAPIView,
    BuyOrderAPIView,
    GetOrderAPIView,
)

app_name = "api"

urlpatterns = [
    path("buy/<int:item_id>/", BuyItemAPIView.as_view(), name="buy_item"),
    path("items/<int:item_id>/", GetItemAPIView.as_view(), name="get_item"),
    path(
        "orders/buy/<int:order_id>/",
        BuyOrderAPIView.as_view(),
        name="buy_order",
    ),
    path(
        "orders/<int:order_id>/", GetOrderAPIView.as_view(), name="get_order"
    ),
]
