from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert '/login' in self.browser.current_url, 'Current URL have no "login"'
       

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN), "Login is not presented"
        assert self.is_element_present(*LoginPageLocators.PASS), "Password is not presented"
        assert self.is_element_present(*LoginPageLocators.ENTER_BUTTON), "Log in is not presented"


    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_ADDRES), "Login is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS), "Password area is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_REPEAT_PASS), "'Confirm password' is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_BUTTON), "Register button is not presented"