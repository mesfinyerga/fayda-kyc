import os
import stripe
import requests
from typing import Dict, Any

stripe.api_key = os.environ.get('STRIPE_API_KEY')
CHAPA_API_KEY = os.environ.get('CHAPA_API_KEY')
TELEBIRR_API_KEY = os.environ.get('TELEBIRR_API_KEY')

# Stripe Payment

def create_stripe_payment(amount: int, currency: str, metadata: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create a Stripe PaymentIntent.
    """
    intent = stripe.PaymentIntent.create(
        amount=amount,  # in cents
        currency=currency,
        metadata=metadata,
    )
    return intent

# Chapa Payment

def create_chapa_payment(amount: float, currency: str, tx_ref: str, return_url: str, metadata: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create a Chapa payment request.
    """
    url = 'https://api.chapa.co/v1/transaction/initialize'
    headers = {'Authorization': f'Bearer {CHAPA_API_KEY}'}
    data = {
        'amount': amount,
        'currency': currency,
        'tx_ref': tx_ref,
        'return_url': return_url,
        **metadata
    }
    resp = requests.post(url, json=data, headers=headers)
    return resp.json()

# Telebirr Payment (starter)
def create_telebirr_payment(amount: float, phone: str, tx_ref: str, metadata: Dict[str, Any]) -> Dict[str, Any]:
    """
    Create a Telebirr payment request (mock/starter).
    """
    # Replace with actual Telebirr API integration
    return {
        'status': 'pending',
        'tx_ref': tx_ref,
        'amount': amount,
        'phone': phone,
        'metadata': metadata
    } 