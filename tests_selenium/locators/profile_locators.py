from selenium.webdriver.common.by import By


class ProfileLocators:
    # Профиль
    INPUT_IMG_FILE = (By.XPATH, "//input[@type='file']")
    BUTTON_SUBMIT = (By.XPATH, "//input[@type='submit']")
    PROFILE_IMG = (By.XPATH, "//div[@class='col-md-4 center']/img")
