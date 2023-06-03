from pages.base_page import BasePage
from locators.user_authorization_locators import UserAuthorizationLocators
import time

class AuthorizationPage(BasePage):
    def authorization(self, email, password):
        self.element_is_visible(UserAuthorizationLocators.INPUT_EMAIL).send_keys(email)
        self.element_is_visible(UserAuthorizationLocators.INPUT_PASSWORD).send_keys(password)
        self.element_is_visible(UserAuthorizationLocators.BUTTON_AUTHORIZATION).click()
        result = self.element_is_visible(UserAuthorizationLocators.USER_LOGIN).text
        return result