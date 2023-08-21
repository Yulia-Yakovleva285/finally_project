
from .base_page import BasePage
from .locators import BasketPageLocators, ProductPageLocators


class BasketPage(BasePage):
    def should_be_text_basket_is_empty (self):
        assert self.is_element_present(*BasketPageLocators.LINK_EMPTY_BASKET), "Basket isn`t empty!"


    def shoud_not_be_goods(self):
        assert self.is_not_element_present(*ProductPageLocators.BOOK_NAME_INTO_BASKET), "Books in the basket!!"