from rest_framework import viewsets, permissions
from .models import Subscription, Payment
from .serializers import SubscriptionSerializer, PaymentSerializer
from core.permissions import IsOrganizationAdmin
from rest_framework.decorators import action
from .gateways import create_stripe_payment, create_chapa_payment, create_telebirr_payment
from rest_framework.response import Response

class SubscriptionViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing subscriptions (org admin only).
    """
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated, IsOrganizationAdmin]

    def get_queryset(self):
        org = self.request.user.organization
        return Subscription.objects.filter(organization=org)

class PaymentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing payments (org users).
    """
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        org = self.request.user.organization
        return Payment.objects.filter(organization=org)

    @action(detail=False, methods=['post'], url_path='initiate-stripe')
    def initiate_stripe(self, request):
        """
        Initiate a Stripe payment.
        """
        amount = int(request.data['amount'])
        currency = request.data.get('currency', 'usd')
        metadata = request.data.get('metadata', {})
        intent = create_stripe_payment(amount, currency, metadata)
        return Response({'client_secret': intent['client_secret']})

    @action(detail=False, methods=['post'], url_path='initiate-chapa')
    def initiate_chapa(self, request):
        """
        Initiate a Chapa payment.
        """
        amount = float(request.data['amount'])
        currency = request.data.get('currency', 'ETB')
        tx_ref = request.data['tx_ref']
        return_url = request.data['return_url']
        metadata = request.data.get('metadata', {})
        resp = create_chapa_payment(amount, currency, tx_ref, return_url, metadata)
        return Response(resp)

    @action(detail=False, methods=['post'], url_path='initiate-telebirr')
    def initiate_telebirr(self, request):
        """
        Initiate a Telebirr payment (mock/starter).
        """
        amount = float(request.data['amount'])
        phone = request.data['phone']
        tx_ref = request.data['tx_ref']
        metadata = request.data.get('metadata', {})
        resp = create_telebirr_payment(amount, phone, tx_ref, metadata)
        return Response(resp) 