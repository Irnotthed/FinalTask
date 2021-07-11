from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        url = self.browser.current_url
        assert self.is_part_of_url("login"),\
            f"Expected login page, but got {url}"


    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_presented(*LoginPageLocators.LOGIN_FORM), \
            "Expected Login form, but found nothing"


    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_presented(*LoginPageLocators.REGISTER_FORM),\
            "Expected Registerform, but found nothing"