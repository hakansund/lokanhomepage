from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User

class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        self.user = User.objects.create_user('kalle', 'email@email.com', 'password')

    def tearDown(self):
        self.browser.quit()

    def test_start_page_layout(self):

        # Kalle is excited to visit Lokan's home page!
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # He sees he has come to the right place.
        self.assertIn('Lokan', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Lokan', header_text)

        # He likes the cool logo that's centered on the index page.
        logo = self.browser.find_element_by_tag_name('img')
        self.assertAlmostEqual(
        logo.location['x'] + logo.size['width'] / 2, 512, delta=5
        )

        # He clicks the about page to learn more about this awesomeness.
        self.browser.get(self.live_server_url + '/about')
        body_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('Om lokan.org', body_text)

        # Next he tries to login.
        self.browser.get(self.live_server_url + '/login')
        usernamebox = self.browser.find_element_by_id('id_username')
        usernamebox.send_keys('kalle')
        passwordnamebox = self.browser.find_element_by_id('id_password')
        passwordnamebox.send_keys('password')
        passwordnamebox.send_keys(Keys.ENTER)
        body_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('Logga ut', body_text)
