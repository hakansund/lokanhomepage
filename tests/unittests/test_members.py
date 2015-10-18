response_url = '/members/'


def test_members_page(response):
    assert response.status_code == 200
