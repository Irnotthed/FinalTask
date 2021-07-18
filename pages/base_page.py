import math
from .locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, browser, url, timeout=12):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_cart_page(self):
        button = self.browser.find_element(*BasePageLocators.CART_BUTTON)
        button.click()

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_cart_button(self):
        assert self.is_element_presented(*BasePageLocators.CART_BUTTON), "Cart button is not presented"

    def should_be_login_url(self):
        assert self.is_element_presented(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        assert self.is_element_presented(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
    def is_element_presented(self, method, element):
        try:
            self.browser.find_element(method, element)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_presented(self, method, element, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((method, element)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, method, element, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((method, element)))
        except TimeoutException:
            return False

        return True

    def is_part_of_url(self, part):
        if part in self.browser.current_url:
            return True
        else:
            return False

    def open(self):
        self.browser.get(self.url)

    def  solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")