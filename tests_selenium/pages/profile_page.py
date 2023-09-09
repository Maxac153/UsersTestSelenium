from tests_selenium.locators.profile_locators import ProfileLocators
from tests_selenium.pages.base_page import BasePage
import time

class ProfilePage(BasePage):
    def replace_avatar(self, img: str):
        """Изменение аватара польлзователя"""

        self.element_is_visible(ProfileLocators.INPUT_IMG_FILE).send_keys(img)
        self.element_is_visible(ProfileLocators.BUTTON_SUBMIT).click()
        time.sleep(3)
        result = self.element_is_visible(ProfileLocators.PROFILE_IMG).get_attribute("src")
        return result
