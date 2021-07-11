link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    navigate_to_login_page(browser)


def navigate_to_login_page(browser):
    login_url = browser.find_element_by_css_selector("#login_link")
    login_url.click()