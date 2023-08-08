from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    REG_ADDRES = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASS = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_REPEAT_PASS = (By.CSS_SELECTOR, "id_registration-password2")
    REG_BUTTON = (By.CSS_SELECTOR, "btn.btn-lg.btn-primary")
    LOGIN = (By.CSS_SELECTOR, "#id_login-username")
    PASS = (By.CSS_SELECTOR, "#id_login-password")
    FORGOT_PASS = (By.LINK_TEXT("Я забыл пароль"))
    ENTER_BUTTON = (By.CSS_SELECTOR, "btn.btn-lg.btn-primary")
