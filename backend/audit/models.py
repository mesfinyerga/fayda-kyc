from django.db import models
from core.models import Organization, User
from typing import Optional

class AuditLog(models.Model):
    """
    Audit log for tracking actions by users in organizations.
    """
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='audit_logs')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='audit_logs')
    action = models.CharField(max_length=255)
    details = models.JSONField(default=dict, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.organization} - {self.action} by {self.user}" 