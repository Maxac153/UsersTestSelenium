from selenium.webdriver.common.by import By

class UserAuthorizationLocators:
    INPUT_EMAIL = (By.XPATH, "//div[@class='col-md-6'][1]/*/*/*/tr[1]/td[2]/input")
    INPUT_PASSWORD = (By.XPATH, "//div[@class='col-md-6'][1]/*/*/*/tr[2]/td[2]/input")
    BUTTON_AUTHORIZATION = (By.XPATH, "//div[@class='col-md-6'][1]/*/*/*/tr[3]/td[2]/input")
    USER_LOGIN = (By.XPATH, "//a[@class='dropdown-toggle']")