from datetime import datetime, timedelta

username = 'kalle'
password = 'fantasy'


def test_add_activity(
        browser, live_server, authorized_user, action_chains, keys):
    # Kalle is planning a board game night, so he enters lokan.org.
    browser.get(live_server.url)
    # He logs in.
    browser.get(live_server.url + '/login')
    usernamebox = browser.find_element_by_id('id_username')
    usernamebox.send_keys(username)
    passwordnamebox = browser.find_element_by_id('id_password')
    passwordnamebox.send_keys(password)
    passwordnamebox.send_keys(keys.ENTER)
    # He hovers on 'Aktiviteter' and clicks 'Skapa aktivitet'.
    activity_menu = browser.find_element_by_xpath(
        '/html/body/nav/section/ul[2]/li[1]/a')
    create_activity_button = browser.find_element_by_xpath(
        '/html/body/nav/section/ul[2]/li[1]/ul/li[4]/a')
    action_chains.move_to_element(activity_menu).click(
        create_activity_button).perform()
    # He enters the values.
    datetimebox = browser.find_element_by_id('id_datetime')
    placebox = browser.find_element_by_id('id_place')
    activitybox = browser.find_element_by_id('id_activity')
    notesbox = browser.find_element_by_id('id_notes')
    datetimebox.send_keys(str(datetime.now() + timedelta(days=3)))
    placebox.send_keys('Kalle')
    activitybox.send_keys('Brädspel')
    notesbox.send_keys('BYOB')
    browser.find_element_by_xpath('//input[@type="submit"]').click()
    body_text = browser.find_element_by_tag_name('body').text
    assert 'Lista över kommande aktiviteter' in body_text
    # And sees a list of upcoming activities.
    body_text = browser.find_element_by_tag_name('body').text
    assert 'Lista över kommande aktiviteter' in body_text
    # Kalle sees that there is an upcoming RPG-night in three days. Awesome!

    # "When was the last board game night?" He clicks on 'Gamla Aktiviteter'.
    assert 0
