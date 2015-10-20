import datetime
import pytest

response_url = '/activities/add/'


def test_activities_create_status_code(response):
    assert response.status_code == 200


def test_activities_create_template(response):
    rendered_templates = tuple(
        templates.name for templates in response.templates)
    assert 'activities/activity_form.html' in rendered_templates


def test_activities_create_content(response):
    assert 'Skapa aktivitet' in response.content.decode('utf-8')


def test_activities_create_as_anonymous_user(anonymous_response):
    assert anonymous_response.status_code == 302


@pytest.mark.django_db()
def test_activities_create_incomplete(authorized_client, authorized_user):
    response = authorized_client.post(response_url, {})
    assert response.status_code == 200


@pytest.mark.django_db()
def test_activities_create_complete(authorized_client, authorized_user):
    data = {'datetime': datetime.datetime.now(), 'place': 'place',
            'activity': 'activity', 'notes': 'notes'}
    response = authorized_client.post(response_url, data)
    assert response.status_code == 302
