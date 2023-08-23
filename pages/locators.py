from selenium.webdriver.common.by import By


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
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group > a.btn.btn-default")
    LINK_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p > a")


class RegisterPageLocators():
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button.btn.btn-lg.btn-primary")