import pytest

response_url = '/activities/old/'


def test_activities_old_status_code(response):
    assert response.status_code == 200


def test_activities_old_template(response):
    rendered_templates = tuple(
        templates.name for templates in response.templates)
    assert 'activities/activity_list.html' in rendered_templates


def test_activities_old_content(response):
    assert 'Gamla aktiviteter' in response.content.decode('utf-8')


@pytest.mark.django_db
def test_activities_old_content_with_activity(old_activity, response):
    assert old_activity.activity in response.content.decode('utf-8')
