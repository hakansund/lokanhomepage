response_url = '/activities/'


def test_activities_upcoming_status_code(response):
    assert response.status_code == 200


def test_activities_upcoming_template(response):
    rendered_templates = tuple(
        templates.name for templates in response.templates)
    assert 'activities/activity_list.html' in rendered_templates


def test_activities_upcoming_content(response):
    assert 'Kommande aktiviteter' in response.content.decode('utf-8')