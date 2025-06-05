from django.db import models
from core.models import Organization
from typing import Optional

class Subscription(models.Model):
    """
    Subscription plan for an organization.
    """
    PLAN_CHOICES = [
        ('free', 'Free'),
        ('pro', 'Pro'),
        ('enterprise', 'Enterprise'),
    ]
    organization = models.OneToOneField(Organization, on_delete=models.CASCADE, related_name='subscription')
    plan = models.CharField(max_length=32, choices=PLAN_CHOICES)
    quota = models.PositiveIntegerField(default=100)
    usage = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=32, default='active')
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.organization} - {self.plan}"

class Payment(models.Model):
    """
    Payment record for an organization (Stripe, Chapa, Telebirr).
    """
    GATEWAY_CHOICES = [
        ('stripe', 'Stripe'),
        ('chapa', 'Chapa'),
        ('telebirr', 'Telebirr'),
    ]
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=8, default='ETB')
    gateway = models.CharField(max_length=32, choices=GATEWAY_CHOICES)
    status = models.CharField(max_length=32)
    transaction_id = models.CharField(max_length=128, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    metadata = models.JSONField(default=dict, blank=True)

    def __str__(self) -> str:
        return f"{self.organization} - {self.amount} {self.currency} ({self.gateway})" 