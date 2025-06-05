from rest_framework import serializers
from .models import Organization, User

class OrganizationSerializer(serializers.ModelSerializer):
    """
    Serializer for Organization model.
    """
    class Meta:
        model = Organization
        fields = ['id', 'name', 'settings', 'branding', 'created_at', 'updated_at']

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    """
    organization = OrganizationSerializer(read_only=True)
    organization_id = serializers.PrimaryKeyRelatedField(
        queryset=Organization.objects.all(), source='organization', write_only=True
    )

    class Meta:
        model = User
        fields = [
            'id', 'email', 'full_name', 'role', 'is_active', 'is_staff', 'date_joined',
            'organization', 'organization_id'
        ]
        read_only_fields = ['is_staff', 'date_joined'] 