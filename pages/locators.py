from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REGISTER_FORM = (By.ID, "register_form")
    LOGIN_FORM = (By.ID, "login_form")


class ProductPageLocators():
    BUTTON_ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    PRODUCT_MESSAGE_BOX = (By.XPATH, "//div[@id='messages']/div[1]/div")
    PRODUCT_MESSAGE_TEXT = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
    CART_MESSAGE_BOX = (By.XPATH, "//div[@id='messages']/div[3]/div")
    CART_MESSAGE_TEXT = (By.XPATH, "//div[@id='messages']/div[3]/div/p/strong")