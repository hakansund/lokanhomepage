import pytest

response_url = '/funding/'

@pytest.mark.django_db
def test_funding_page(response):
    assert response.status_code == 200
