from django.urls import path

from .views import BuyItemAPIView, GetItemAPIView
app_name = 'api'

urlpatterns = [
    path("buy/<int:item_id>/", BuyItemAPIView.as_view(), name="buy_item"),
    path("get/<int:item_id>/", GetItemAPIView.as_view(), name="get_item"),
]