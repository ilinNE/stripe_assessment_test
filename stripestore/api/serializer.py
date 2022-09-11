from dataclasses import field
from rest_framework import serializers

from store.models import Order, Item, ItemInOrder


class ItemInOrderSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("item", "quantity")


class OrderSerializer(serializers.ModelSerializer):
    items = ItemInOrderSerializer(many=True, source="iteminorder_set")

    class Meta:
        model = Order
        fields = "items"
