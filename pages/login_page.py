from .base_page import BasePage
from .locators import LoginPageLocators, RegisterPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
        self.register_new_user()

    def should_be_login_url(self):
        assert '/login' in self.browser.current_url, 'Current URL have no "login"'
       

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN), "Login is not presented"
        assert self.is_element_present(*LoginPageLocators.PASS), "Password is not presented"
        assert self.is_element_present(*LoginPageLocators.ENTER_BUTTON), "Log in is not presented"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_ADDRES), "Login is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS), "Password area is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_REPEAT_PASS), "'Confirm password' is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_BUTTON), "Register button is not presented"


    def register_new_user(self, email, password):
        email_area = self.browser.find_element(*RegisterPageLocators.EMAIL)
        email_area.send_keys(email)
        password_area = self.browser.find_element(*RegisterPageLocators.PASSWORD)
        password_area.send_keys(password)
        confirm_password_area = self.browser.find_element(*RegisterPageLocators.CONFIRM_PASSWORD)
        confirm_password_area.send_keys(password)
        register_button = self.browser.find_element(*RegisterPageLocators.REGISTER_BUTTON)
        register_button.click()
        


