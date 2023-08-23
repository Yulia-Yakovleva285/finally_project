import time
import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage

#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"])
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  #pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

   

@pytest.mark.xfail
def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.click_button()
    page.success_message_should_disappear()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95"
    page = ProductPage(browser, link)
    page.open()
    page.click_basket_button()
    page = BasketPage(browser, browser.current_url)
    page.should_be_text_basket_is_empty()
    page.shoud_not_be_goods()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = ProductPage(browser, link)
        page.open()
        page.click_button()
        page.should_not_be_success_message()

def test_guest_can_add_product_to_basket(browser, link):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                 #открываем страницу
        page.click_button()         #клик добавить в корзину
        page.solve_quiz_and_get_code() #считаем и отправляем ответ
        time.sleep(120)
        page.should_be_same_price()
        time.sleep(120)
        page.should_be_same_book_name()
        time.sleep(5)


@pytest.mark.register
class TestUserAddToBasketFromProductPage():
    @pytest.fixture (scope = "function", autouse=True)
    def setup(self, browser):
        link = 'https://selenium1py.pythonanywhere.com/accounts/login/'
        page = ProductPage(browser, link)
        page.open() 
        page.go_to_login_page()
        page = LoginPage(browser, browser.current_url)  
        email = str(time.time()) + "@fakemail.org"
        password = 'blablabla100500'
        page.register_new_user(email, password)    
        page.should_be_authorized_user()


    def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = ProductPage(browser, link)
        page.open()
        time.sleep(3)
        page.click_button()
        time.sleep(3)
        page.should_not_be_success_message()


    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                 #открываем страницу
        page.click_button()         #клик добавить в корзину
        #page.solve_quiz_and_get_code() #считаем и отправляем ответ
        #time.sleep(120)
        page.should_be_same_price()
        #time.sleep(120)
        page.should_be_same_book_name()
        #time.sleep(5)