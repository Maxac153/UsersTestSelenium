import pytest
import allure

from selenium import webdriver

from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(scope='session', autouse=True)
def driver():
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.quit()

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
