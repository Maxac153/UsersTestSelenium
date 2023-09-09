from tests_selenium.pages.base_page import BasePage
from tests_selenium.locators.authorization_and_registration_locators import \
    AuthorizationAndRegistrationLocators


class AuthorizationAndRegistrationPage(BasePage):
    def authorization(self, email: str, password: str) -> None:
        self.element_is_visible(AuthorizationAndRegistrationLocators.LOGIN_INPUT_USER_EMAIL).send_keys(email)
        self.element_is_visible(AuthorizationAndRegistrationLocators.LOGIN_INPUT_USER_PASSWORD).send_keys(password)
        self.element_is_visible(AuthorizationAndRegistrationLocators.BUTTON_USER_AUTHORIZATION).click()

    def registration(self, name: str, email: str, password: str) -> None:
        self.element_is_visible(AuthorizationAndRegistrationLocators.REG_INPUT_USER_NAME).send_keys(name)
        self.element_is_visible(AuthorizationAndRegistrationLocators.REG_INPUT_USER_EMAIL).send_keys(email)
        self.element_is_visible(AuthorizationAndRegistrationLocators.REG_INPUT_USER_PASSWORD).send_keys(password)
        self.element_is_visible(AuthorizationAndRegistrationLocators.BUTTON_USER_REG).click()
