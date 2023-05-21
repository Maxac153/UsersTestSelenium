from selenium.webdriver.common.by import By

class UserAvatarProfile:
    INPUT_EMAIL = (By.XPATH, "//div[@class='col-md-6'][1]/*/*/*/tr[1]/td[2]/input")
    INPUT_PASSWORD = (By.XPATH, "//div[@class='col-md-6'][1]/*/*/*/tr[2]/td[2]/input")
    BUTTON_AUTHORIZATION = (By.XPATH, "//div[@class='col-md-6'][1]/*/*/*/tr[3]/td[2]/input")
    USER_LOGO = (By.XPATH, "//li/a[@class='dropdown-toggle']")
    USER_PERSONAL_ACCOUNT = (By.XPATH, "//li/a[@href='/user/profile/index.html']")
    USER_ICON_INPUT = (By.XPATH, "//td//input[@type='file']")
    USER_SAVE_ICON = (By.XPATH, "//td/input[@type='submit']")
    USER_ICON = (By.XPATH, "//div/img")