from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_text(self):
        assert self.is_element_presented(*BasketPageLocators.EMPTY_LABEL), "Expected empty basket text," \
                                                                           " but found nothing"

    def should_not_be_basket_items(self):
        assert self.is_not_element_presented(*BasketPageLocators.BASKET_ITEMS), "Expected no items in basket," \
                                                                                "but found some"