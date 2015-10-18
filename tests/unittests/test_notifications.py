response_url = '/notifications/'


def test_notifications_page(response):
    assert response.status_code == 200
