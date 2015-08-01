import pytest
from django.contrib.auth.models import User

def create_user(username='username', email='email@email.com', password='password'):
    return User.objects.create_user(username, email,  password)

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_about_page(client):
    response = client.get('/about/')
    assert response.status_code == 200

def test_login_page(client):
    response = client.get('/login/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_login_nonuser(client):
    user = create_user()
    response = client.login(username='Kalle', password='')
    assert response is False

@pytest.mark.django_db
def test_login_wrong_password(client):
    user = create_user()
    response = client.login(username='username', password='wrongpass')
    assert response is False

@pytest.mark.django_db
def test_login_user(client):
    user = create_user()
    response = client.login(username='username', password='password')
    assert response is True
