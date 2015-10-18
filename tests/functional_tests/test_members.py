import pytest

response_url = '/members/'

@pytest.mark.django_db
def test_members_page(response):
    assert response.status_code == 200
