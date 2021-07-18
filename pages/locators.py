from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_BUTTON = (By.XPATH, "//span[@class='btn-group']/a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    HEADER_NAME = (By.TAG_NAME, "h1")
    EMPTY_LABEL = (By.TAG_NAME, "p")
    BASKET_ITEMS = (By.XPATH, "//div[@class='basket-items']")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REGISTER_FORM = (By.ID, "register_form")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_EMAIL = (By.XPATH, "//input[@name='registration-email']")
    REGISTRATION_PASSWORD = (By.XPATH, "//input[@name='registration-password1']")
    REGISTRATION_PASSWORD_CONFIRM = (By.XPATH, "//input[@name='registration-password2']")
    REGISTER_BUTTON = (By.XPATH, "//button[@name='registration_submit']")


class ProductPageLocators():
    BUTTON_ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    PRODUCT_MESSAGE_BOX = (By.XPATH, "//div[@id='messages']/div[1]/div")
    PRODUCT_MESSAGE_TEXT = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
    CART_MESSAGE_BOX = (By.XPATH, "//div[@id='messages']/div[3]/div")
    CART_MESSAGE_TEXT = (By.XPATH, "//div[@id='messages']/div[3]/div/p/strong")