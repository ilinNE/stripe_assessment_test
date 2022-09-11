from webbrowser import get
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
import stripe

from store.models import Item

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
                    "quantity": 2,
                    "tax_rates": ["txr_1LgeyfHE8R9CM9s42l29F2Aw"],
                    
                }
            ],
            discounts=[{
                'coupon': 'TMeMClay',
            }],
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
