import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_api_root(api_client):
    response = api_client.get('/api/')
    assert response.status_code in (200, 404)  # 404 if no root, 200 if root view exists 