from selenium.webdriver.common.by import By


class BaseLocators:
    # Пользователи
    BUTTON_USERS = (By.XPATH, "//span[text()='Пользователи']")

    # Войти
    BUTTON_LOGIN = (By.XPATH, "//a[@href='/user/login/index.html']")

    # Профиль пользователя
    BUTTON_ICON = (By.XPATH, "//a[@class='dropdown-toggle']")
    BUTTON_PROFILE = (By.XPATH, "//a[@href='/user/profile/index.html']")
    BUTTON_LOGOUT = (By.XPATH, "//a[@href='/user/logout.html']")

    # Пользователи
    INPUT_NAME_OR_EMAIL = (By.XPATH, "//input[@placeholder='Введите email или имя']")
    BUTTON_SEARCH = (By.XPATH, "//button[@class='btn btn-submit']")
    BUTTON_DELETE = (By.XPATH, "//a[text()='Удалить']")
