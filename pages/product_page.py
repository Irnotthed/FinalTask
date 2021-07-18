from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    def should_add_to_cart(self):
        button_add_to_cart = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
        button_add_to_cart.click()
        BasePage.solve_quiz_and_get_code(self)

        product_message_box = WebDriverWait(self.browser,10).until(
                EC.presence_of_element_located((ProductPageLocators.PRODUCT_MESSAGE_BOX)))
        cart_message_box = WebDriverWait(self.browser,10).until(
                EC.presence_of_element_located((ProductPageLocators.CART_MESSAGE_BOX)))

        product_message_text = self.browser.find_element(*ProductPageLocators.PRODUCT_MESSAGE_TEXT).text
        cart_message_text = self.browser.find_element(*ProductPageLocators.CART_MESSAGE_TEXT).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

        assert product_message_text == product_name, f"Invalid product name, " \
                                                               f"expected {product_name}," \
                                                               f" but got {product_message_text}"
        assert cart_message_text == product_price, f"Invalid total price," \
                                                              f" expected {product_price}," \
                                                              f" but got {cart_message_text}"