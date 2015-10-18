response_url = '/funding/'


def test_funding_page1(response):
    assert response.status_code == 200
