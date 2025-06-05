from django.db import models
from core.models import Organization, User
from typing import Optional

class Verification(models.Model):
    """
    Represents a Fayda KYC verification request and response.
    """
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='verifications')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='verifications')
    fayda_id = models.CharField(max_length=64)
    request_payload = models.JSONField()
    response_payload = models.JSONField(null=True, blank=True)
    status = models.CharField(max_length=32, choices=[('pending', 'Pending'), ('success', 'Success'), ('failed', 'Failed')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Verification {self.fayda_id} ({self.status})" 