from pages.base_page import BasePage
from locators.user_profile_locators import UserAvatarProfile
import time

class ProfilePage(BasePage):
    def authorization(self, email, password, img):
        self.element_is_visible(UserAvatarProfile.INPUT_EMAIL).send_keys(email)
        self.element_is_visible(UserAvatarProfile.INPUT_PASSWORD).send_keys(password)
        self.element_is_visible(UserAvatarProfile.BUTTON_AUTHORIZATION).click()
        time.sleep(3)
        self.element_is_visible(UserAvatarProfile.USER_LOGO).click()
        self.element_is_visible(UserAvatarProfile.USER_PERSONAL_ACCOUNT).click()
        self.element_is_visible(UserAvatarProfile.USER_ICON_INPUT).send_keys(img)
        self.element_is_visible(UserAvatarProfile.USER_SAVE_ICON).click()
        time.sleep(3)
        result = self.element_is_visible(UserAvatarProfile.USER_ICON).get_attribute("src")
        return result