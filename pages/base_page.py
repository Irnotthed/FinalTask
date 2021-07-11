from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, browser, url, timeout=12):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_presented(self, method, element):
        try:
            self.browser.find_element(method, element)
        except NoSuchElementException:
            return False
        return True

    def is_part_of_url(self, part):
        if part in self.browser.current_url:
            return True
        else:
            return False