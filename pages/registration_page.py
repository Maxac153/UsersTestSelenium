from pages.base_page import BasePage
from locators.user_registration_locators import UserRegistrationLocators

class RegistrationPage(BasePage):
    def registration_and_submit(self, first_name, email, password):
        self.element_is_visible(UserRegistrationLocators.INPUT_NAME).send_keys(first_name)
        self.element_is_visible(UserRegistrationLocators.INPUT_EMAIL).send_keys(email)
        self.element_is_visible(UserRegistrationLocators.INPUT_PASSWORD).send_keys(password)
        self.element_is_visible(UserRegistrationLocators.BUTTON_REGISTRATION).click()