from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        """Открытие страницы"""

        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5):
        """Найти один элемент на странице"""

        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        """Найти все элементы на странице"""

        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def class_attribute(self, locator, timeout=5):
        """Параметры атрибута"""

        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def drag_and_drop(self, drag, drop):
        """Перемещение элемента"""

        ActionChains(self.driver).drag_and_drop(drag, drop).perform()

    def action_chains(self):
        """Возврат объект ActionChains движения мыши"""

        return ActionChains(self.driver)