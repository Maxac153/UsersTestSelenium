from selenium.webdriver.common.by import By


class AuthorizationAndRegistrationLocators:
    # Авторизация
    LOGIN_INPUT_USER_EMAIL = (By.XPATH, "//input[@name='login']")
    LOGIN_INPUT_USER_PASSWORD = (By.XPATH, "//input[@name='password']")
    BUTTON_USER_AUTHORIZATION = (By.XPATH, "//input[@value='Авторизоваться']")

    # Регистрация
    REG_INPUT_USER_NAME = (By.XPATH, "//input[@required=''][@name='name']")
    REG_INPUT_USER_EMAIL = (By.XPATH, "//input[@required=''][@name='email']")
    REG_INPUT_USER_PASSWORD = (By.XPATH, "//input[@name='password'][@required='']")
    BUTTON_USER_REG = (By.XPATH, "//input[@value='Зарегистрироваться']")
