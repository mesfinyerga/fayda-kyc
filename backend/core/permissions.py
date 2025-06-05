from rest_framework import permissions

class IsOrganizationAdmin(permissions.BasePermission):
    """
    Allows access only to organization admins.
    """
    def has_permission(self, request, view):
        return hasattr(request.user, 'role') and request.user.role == 'admin'

class IsVerifier(permissions.BasePermission):
    """
    Allows access to verifiers and admins.
    """
    def has_permission(self, request, view):
        return hasattr(request.user, 'role') and request.user.role in ['admin', 'verifier']

class IsViewer(permissions.BasePermission):
    """
    Allows access to viewers, verifiers, and admins.
    """
    def has_permission(self, request, view):
        return hasattr(request.user, 'role') and request.user.role in ['admin', 'verifier', 'viewer'] 