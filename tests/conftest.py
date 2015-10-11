import pytest
#from model_mommy import mommy
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from xvfbwrapper import Xvfb

@pytest.fixture(scope="module")
def browser(request):
    xvfb = Xvfb()
    xvfb.start()
    driver = Firefox()
    request.addfinalizer(driver.quit)
    request.addfinalizer(xvfb.stop)
    return driver

@pytest.fixture(scope="module")
def keys():
    return Keys()

@pytest.fixture()
def response(client, request):
    return client.get(request.module.response_url)

@pytest.fixture()
def authorized_user(django_user_model, request):
    return django_user_model.objects.create_user(
        username=request.module.username,
        password=request.module.password)
