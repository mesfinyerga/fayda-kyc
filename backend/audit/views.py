from rest_framework import viewsets, permissions
from .models import AuditLog
from .serializers import AuditLogSerializer
from core.permissions import IsOrganizationAdmin

class AuditLogViewSet(viewsets.ModelViewSet):
    """
    ViewSet for audit logs (org admin only).
    """
    serializer_class = AuditLogSerializer
    permission_classes = [permissions.IsAuthenticated, IsOrganizationAdmin]

    def get_queryset(self):
        org = self.request.user.organization
        return AuditLog.objects.filter(organization=org)

    def perform_create(self, serializer):
        log = serializer.save(organization=self.request.user.organization, user=self.request.user)
        # Example: log the creation
        log.details['event'] = 'created'
        log.save()
        return log

    def perform_update(self, serializer):
        log = serializer.save()
        log.details['event'] = 'updated'
        log.save()
        return log

    def perform_destroy(self, instance):
        # Example: log the deletion (could be extended to a soft delete)
        instance.details['event'] = 'deleted'
        instance.save()
        instance.delete() 