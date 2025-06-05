from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Verification
from .serializers import VerificationSerializer
from core.permissions import IsVerifier
from payments.models import Subscription

class VerificationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for KYC verifications. Only verifiers and admins can access.
    """
    serializer_class = VerificationSerializer
    permission_classes = [permissions.IsAuthenticated, IsVerifier]

    def get_queryset(self):
        org = self.request.user.organization
        return Verification.objects.filter(organization=org)

    def perform_create(self, serializer):
        org = self.request.user.organization
        sub = Subscription.objects.get(organization=org)
        if sub.usage >= sub.quota:
            raise Exception('Quota exceeded for this subscription plan.')
        verification = serializer.save(organization=org, user=self.request.user)
        sub.usage += 1
        sub.save()
        return verification 