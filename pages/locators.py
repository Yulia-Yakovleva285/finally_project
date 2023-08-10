from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REG_ADDRES = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_REPEAT_PASS = (By.CSS_SELECTOR, "id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "btn.btn-lg.btn-primary")
    LOGIN = (By.CSS_SELECTOR, "#id_login-username")
    PASS = (By.CSS_SELECTOR, "#id_login-password")
    ENTER_BUTTON = (By.CSS_SELECTOR, "btn.btn-lg.btn-primary")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    
    BOOK_NAME_INTO_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) strong")
    
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BOOK_PRICE_INTO_BASKET = (By.CSS_SELECTOR, ".alertinner > p strong")
  

