from webbrowser import get
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
import stripe

from store.models import Item, Order

stripe.api_key = settings.STRIPE_SECRET_KEY


class BuyItemAPIView(APIView):
    def get(self, request, item_id):
        item = get_object_or_404(Item, id=item_id)
        session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price_data": {
                        "currency": "rub",
                        "product_data": {
                            "name": item.name,
                            "description": item.descpiption,
                        },
                        "unit_amount": item.price,
                    },
                    "quantity": 1,
                    "tax_rates": ["txr_1LgeyfHE8R9CM9s42l29F2Aw"],
                }
            ],
            mode="payment",
            success_url="https://example.com/success",
            cancel_url="https://example.com/cancel",
        )
        data = {"session_id": session.id}
        return Response(data)


class GetItemAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "get_item.html"

    def get(self, request, item_id):
        item = get_object_or_404(Item, id=item_id)
        data = {"item": item, "stripe_key": settings.STRIPE_PUBLIC_KEY}
        response: Response = Response(data)
        return response


class BuyOrderAPIView(APIView):
    def get(self, request, order_id):
        order = get_object_or_404(
            Order.objects.select_related("tax", "discount"), id=order_id
        )
        line_items = []
        for item_in_order in order.iteminorder_set.select_related(
            "item"
        ).all():
            line_item = {
                "price_data": {
                    "currency": "rub",
                    "product_data": {
                        "name": item_in_order.item.name,
                        "description": item_in_order.item.descpiption,
                    },
                    "unit_amount": item_in_order.item.price,
                },
                "quantity": item_in_order.quantity,
            }
            if order.tax:
                line_item["tax_rates"] = [order.tax.stripe_id]
                line_items.append(line_item)
        session_data = {
            "line_items": line_items,
            "mode": "payment",
            "success_url": "https://example.com/success",
            "cancel_url": "https://example.com/cancel",
        }
        if order.discount:
            session_data["discounts"] = [
                {
                    "coupon": order.discount.coupon_id,
                }
            ]
        session = stripe.checkout.Session.create(**session_data)
        data = {"session_id": session.id}
        return Response(data)


class GetOrderAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "get_order.html"

    def get(self, request, order_id):
        order = get_object_or_404(
            Order.objects.select_related("tax", "discount"), id=order_id
        )
        item_in_orders = order.iteminorder_set.select_related("item").all()
        data = {
            "order": order,
            "item_in_orders": item_in_orders,
            "stripe_key": settings.STRIPE_PUBLIC_KEY,
        }
        response: Response = Response(data)
        return response
