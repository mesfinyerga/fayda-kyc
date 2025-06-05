from rest_framework import serializers
from .models import Verification

class VerificationSerializer(serializers.ModelSerializer):
    """
    Serializer for Verification model.
    """
    class Meta:
        model = Verification
        fields = '__all__' 