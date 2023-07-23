import pytest
import allure

from selenium import webdriver
from pages.logout_page import LogoutPage

@pytest.fixture(scope='session', autouse=True)
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def logout(driver):
    yield
    with allure.step('Выход из под учётной записи'):
        from_page = LogoutPage(driver, 'http://users.bugred.ru/user/login/index.html')
        from_page.open()
        from_page.logout()

@pytest.fixture()
def screenshot(driver):
    yield
    with allure.step('Screenshot'):
        attach = driver.get_screenshot_as_png()
        allure.attach(
            attach,
            name="Screenshot",
            attachment_type=allure.attachment_type.PNG
        )