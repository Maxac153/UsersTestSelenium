from selenium.webdriver.common.by import By

class UserDeleteLocators:
    INPUT_NAME = (By.XPATH, "//div[@class='col-md-6'][1]/*/*/*/tr[1]/td[2]/input")
    INPUT_EMAIL = (By.XPATH, "//div[@class='col-md-6'][1]/*/*/*/tr[2]/td[2]/input")
    BUTTON_AUTHORIZATION = (By.XPATH, "//input[@class='btn btn-danger']")
    INPUT_USER_SEARCH = (By.XPATH, "//input[@placeholder='Введите email или имя']")
    BUTTON_SEARCH = (By.XPATH, "//button[@class='btn btn-submit']")
    BUTTON_DELETE = (By.XPATH, "//a[text()='Удалить']")
    FOUND_USERS = (By.XPATH, "//div[@class='content']/p[2]")