from pages.base_page import BasePage
from locators.user_delete_locators import UserDeleteLocators

class DeletePage(BasePage):
    def delete_user(self, email, password, user_name_delete):
        self.element_is_visible(UserDeleteLocators.INPUT_NAME).send_keys(email)
        self.element_is_visible(UserDeleteLocators.INPUT_EMAIL).send_keys(password)
        self.element_is_visible(UserDeleteLocators.BUTTON_AUTHORIZATION).click()
        self.element_is_visible(UserDeleteLocators.INPUT_USER_SEARCH).send_keys(user_name_delete)
        self.element_is_visible(UserDeleteLocators.BUTTON_SEARCH).click()
        self.element_is_visible(UserDeleteLocators.BUTTON_DELETE).click()
        result = self.element_is_visible(UserDeleteLocators.FOUND_USERS).text
        return result