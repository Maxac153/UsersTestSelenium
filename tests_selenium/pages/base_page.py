from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

from tests_selenium.locators.base_locators import BaseLocators


class BasePage:
    TIMEOUT_SECONDS = 5

    def __init__(self, driver, url: str = ''):
        self.driver = driver
        self.url = url

    def open(self):
        """Открытие страницы"""

        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout: int = TIMEOUT_SECONDS):
        """Найти один элемент на странице"""

        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout: int = TIMEOUT_SECONDS):
        """Найти все элементы на странице"""

        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def class_attribute(self, locator, timeout: int = TIMEOUT_SECONDS):
        """Параметры атрибута"""

        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def into_user_account(self):
        """Войти в профиль пользователя"""

        self.element_is_visible(BaseLocators.BUTTON_ICON).click()
        self.element_is_visible(BaseLocators.BUTTON_PROFILE).click()

    def logout_account(self):
        """Выход из профиля"""

        self.element_is_visible(BaseLocators.BUTTON_ICON).click()
        self.element_is_visible(BaseLocators.BUTTON_LOGOUT).click()

    def delete_user_account(self, user_name_or_email: str):
        """Удаление пользователя (работает только из под Администратора)"""

        self.element_is_visible(BaseLocators.INPUT_NAME_OR_EMAIL).send_keys(user_name_or_email)
        self.element_is_visible(BaseLocators.BUTTON_SEARCH).click()
        self.element_is_visible(BaseLocators.BUTTON_DELETE).click()
