import pytest
import time
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                               marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.skip(reason="no need to test this")
def test_guest_can_add_product_to_basket(browser, link):
    url = link
    page = ProductPage(browser, url)
    page.open()
    page.should_add_to_cart()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, url)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart()
    page.should_be_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, url)
    page.open()
    page.should_be_login_url()


def test_guest_can_go_to_login_page_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, url)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser,browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, url)
    page.open()
    page.go_to_cart_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_basket_items()
    basket_page.should_be_empty_text()


@pytest.mark.user_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, url)
        page.open()
        page.register_new_user(f"{str(time.time())}@testm.org", "qwe123456789")
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, url)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, url)
        page.open()
        page.should_add_to_cart()