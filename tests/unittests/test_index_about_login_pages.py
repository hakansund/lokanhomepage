import pytest

response_url = '/'
def test_index_page(response):
    assert response.status_code == 200


response = '/about/'
def test_about_page(response):
    assert response.status_code == 200


response = '/login/'
def test_login_page(response):
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_nonuser(client, authorized_user):
    response = client.login(username='Kalle', password='_')
    assert response is False


@pytest.mark.django_db
def test_login_wrong_password(client, authorized_user):
    response = client.login(
        username='username', password='wrongpass')
    assert response is False


@pytest.mark.django_db
def test_login_user(client, authorized_user):
    response = client.login(
        username='username', password='password')
    assert response is True
