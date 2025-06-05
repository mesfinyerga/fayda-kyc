import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from core.models import Organization

@pytest.fixture
def organization(db):
    return Organization.objects.create(name="TestOrg")

@pytest.fixture
def user(db, organization):
    User = get_user_model()
    return User.objects.create_user(email="user@test.com", password="testpass123", organization=organization, role="admin")

@pytest.fixture
def api_client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client 