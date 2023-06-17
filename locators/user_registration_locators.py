from selenium.webdriver.common.by import By

class UserRegistrationLocators:
    INPUT_NAME = (By.XPATH, "//div[@class='col-md-6'][2]/*/*/*/tr[1]/td[2]/input")
    INPUT_EMAIL = (By.XPATH, "//div[@class='col-md-6'][2]/*/*/*/tr[2]/td[2]/input")
    INPUT_PASSWORD = (By.XPATH, "//div[@class='col-md-6'][2]/*/*/*/tr[3]/td[2]/input")
    BUTTON_REGISTRATION = (By.XPATH, "//input[@name='act_register_now']")