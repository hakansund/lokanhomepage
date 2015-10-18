import pytest

response_url = '/notifications/'


@pytest.mark.django_db
def test_notifications_page(response):
    assert response.status_code == 200
