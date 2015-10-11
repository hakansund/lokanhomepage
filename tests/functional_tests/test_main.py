username = 'kalle'
password = 'password'

def test_index_page(browser, live_server):
    # Kalle is excited to visit Lokan's home page!
    browser.get(live_server.url)
    # He sees he has come to the right place.
    body_text = browser.find_element_by_tag_name('body').text
    assert 'Välkommen till Lokans hemsida!' in body_text

def test_login(browser, live_server, authorized_user, keys):
    # Next he tries to log in.
    browser.get(live_server.url + '/login')
    usernamebox = browser.find_element_by_id('id_username')
    usernamebox.send_keys(username)
    passwordnamebox = browser.find_element_by_id('id_password')
    passwordnamebox.send_keys(password)
    passwordnamebox.send_keys(keys.ENTER)
    body_text = browser.find_element_by_tag_name('body').text
    assert 'Your username and password didn\'t match' not in body_text

def test_logout(browser, live_server, authorized_user):
    # Will he be able to log out?
    browser.get(live_server.url + '/logout')
    body_text = browser.find_element_by_tag_name('body').text
    assert 'Du är nu utloggad!' in body_text

def test_about_page(browser, live_server):
    # He clicks the about page to learn more about this awesomeness.
    browser.get(live_server.url + '/about')
    body_text = browser.find_element_by_tag_name('body').text
    assert 'Om lokan.org' in body_text
