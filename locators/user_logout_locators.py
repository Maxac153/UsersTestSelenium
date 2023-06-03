from selenium.webdriver.common.by import By
class UserLogoutLocators:
    BUTTON_ICON = (By.XPATH, "//a[@class='dropdown-toggle']")
    BUTTON_LOGOUT = (By.XPATH, "//a[@href='/user/logout.html']")
    