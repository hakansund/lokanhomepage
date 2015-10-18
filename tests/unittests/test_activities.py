response_url = '/activities/'


def test_activities_page(response):
    assert response.status_code == 200


def test_activities_page_template(response):
    rendered_templates = tuple(templates.name for templates in response.templates)
    assert 'activity_list.html' in rendered_templates


response_url = '/activities/old/'


def test_old_activity_page(response):
    assert response.status_code == 200


response_url = '/activities/add/'


def test_create_activity_page(response):
    assert response.status_code == 200


def test_create_activity_page_as_anonymous_user(anonymous_response):
    assert anonymous_response.status_code == 302


def test_create_activity(client, authorized_user):
    client.login(username='username', password='password')
    response = client.post(response_url, {})
    assert response.status_code == 200
    assert "bajs" in str(response.content)
