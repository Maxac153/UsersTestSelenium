import pytest
from selenium import webdriver

from pages.delete_page import DeletePage
from pages.logout_page import LogoutPage

@pytest.fixture(scope='session', autouse=True)
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    browser.quit()

@pytest.fixture()
def delete_user(driver):
    yield
    email = 'manager@mail.ru'
    password = '1'
    user_name_delete = 'tur123'

    from_page = DeletePage(driver, 'http://users.bugred.ru/user/login/index.html')
    from_page.open()
    from_page.delete_user(email, password, user_name_delete)

@pytest.fixture()
def logout(driver):
    yield
    from_page = LogoutPage(driver, 'http://users.bugred.ru/user/login/index.html')
    from_page.open()
    from_page.logout()
