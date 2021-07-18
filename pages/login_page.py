from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        registration_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        registration_email.send_keys(email)
        registration_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD)
        registration_password.send_keys(password)
        registration_password_confirm = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM)
        registration_password_confirm.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert self.is_part_of_url("login"),\
            f"Expected login page, but got {url}"

    def should_be_login_form(self):
        assert self.is_element_presented(*LoginPageLocators.LOGIN_FORM), \
            "Expected Login form, but found nothing"

    def should_be_register_form(self):
        assert self.is_element_presented(*LoginPageLocators.REGISTER_FORM),\
            "Expected Registerform, but found nothing"