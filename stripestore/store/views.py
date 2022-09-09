from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.conf import settings
import stripe


stripe.api_key = settings.STRIPE_KEY

def index(request):
    session = stripe.checkout.Session.create(
    line_items=[{
      'price_data': {
        'currency': 'rub',
        'product_data': {
          'name': 'T-shirt',
        },
        'unit_amount': 2000,
      },
      'quantity': 1,
    }, {
      'price_data': {
        'currency': 'rub',
        'product_data': {
          'name': 'B-shirt',
        },
        'unit_amount': 1200,
      },
      'quantity': 1,
    }],
    mode='payment',
    success_url='https://example.com/success',
    cancel_url='https://example.com/cancel',
    )

    return redirect(session.url, code=303)