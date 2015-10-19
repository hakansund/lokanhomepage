response_url = '/activities/old/'


def test_old_activity_page(response):
    assert response.status_code == 200


def test_old_activity_page_template(response):
    rendered_templates = tuple(
        templates.name for templates in response.templates)
    assert 'activities/activity_list.html' in rendered_templates


def test_old_activity_page_content(response):
    assert 'Gamla aktiviteter' in response.content.decode('utf-8')
