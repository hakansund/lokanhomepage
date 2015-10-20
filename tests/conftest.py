import pytest
from datetime import datetime, timedelta
from model_mommy import mommy
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from xvfbwrapper import Xvfb


@pytest.fixture(scope="module")
def browser(request):
    xvfb = Xvfb(1200, 900)
    xvfb.start()
    driver = Firefox()
    request.addfinalizer(driver.quit)
    request.addfinalizer(xvfb.stop)
    return driver


@pytest.fixture(scope="module")
def keys():
    return Keys()


@pytest.fixture(scope="module")
def action_chains(browser):
    return ActionChains(browser)


@pytest.fixture()
def anonymous_response(client, request):
    return client.get(request.module.response_url)


@pytest.fixture()
def response(client, request, authorized_user):
    client.login(username='username', password='password')
    return client.get(request.module.response_url)


@pytest.fixture()
def authorized_user(django_user_model, request):
    return django_user_model.objects.create_user(
        username=getattr(request.module, 'username', 'username'),
        password=getattr(request.module, 'password', 'password'))


@pytest.fixture()
def old_activity():
    return mommy.make('Activity', datetime=(datetime.now()-timedelta(days=3)))


@pytest.fixture()
def upcoming_activity():
    return mommy.make('Activity', datetime=(datetime.now()+timedelta(days=3)))


@pytest.fixture()
def authorized_client(client, authorized_user):
    client.login(username='username', password='password')
    return client
