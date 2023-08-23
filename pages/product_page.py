from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def click_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET) 
        button.click() 
    
    def should_be_same_price(self):
        book_name = self.value(*ProductPageLocators.BOOK_NAME)
        print(book_name)
        book_name_into_basket = self.value(*ProductPageLocators.BOOK_NAME_INTO_BASKET)
        print(book_name_into_basket)
        assert book_name == book_name_into_basket, "Book name doesn`t match!"
        
    def should_be_same_book_name(self):
        book_price = self.value(*ProductPageLocators.BOOK_PRICE)
        print(book_price)
        book_price_into_basket = self.value(*ProductPageLocators.BOOK_PRICE_INTO_BASKET)
        print(book_price_into_basket)
        assert book_price == book_price_into_basket, "Book price doesn`t match!"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message did`t disappear!"
