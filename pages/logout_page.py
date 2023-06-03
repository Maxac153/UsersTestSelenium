from pages.base_page import BasePage
from locators.user_logout_locators import UserLogoutLocators

class LogoutPage(BasePage):
    def logout(self):
        self.element_is_visible(UserLogoutLocators.BUTTON_ICON).click()
        self.element_is_visible(UserLogoutLocators.BUTTON_LOGOUT).click()