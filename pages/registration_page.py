from pages.base_page import BasePage
from locators.user_registration_locators import UserRegistrationLocators
import time

class RegistrationPage(BasePage):
    def registration_and_submit(self, first_name, email, password):
        self.element_is_visible(UserRegistrationLocators.INPUT_NAME).send_keys(first_name)
        self.element_is_visible(UserRegistrationLocators.INPUT_EMAIL).send_keys(email)
        self.element_is_visible(UserRegistrationLocators.INPUT_PASSWORD).send_keys(password)
        self.element_is_visible(UserRegistrationLocators.BUTTON_REGISTRATION).click()
        time.sleep(3)

    def user_authorization(self):
        return self.element_is_visible(UserRegistrationLocators.USER_LOGIN).text

    def error_message(self):
        return self.element_is_visible(UserRegistrationLocators.ERROR_MESSAGE).text