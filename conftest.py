import pytest
from selenium import webdriver

@pytest.fixture(scope='session', autouse=True)
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--start-maximized")
    browser = webdriver.Chrome(options=chrome_options)
    yield browser
    browser.quit()