import pytest
import allure

from pages.delete_page import DeletePage
from pages.logout_page import LogoutPage
from pages.registration_page import RegistrationPage

@allure.epic('Проверка регистрации')
class TestUserRegistration:
    __test_data = [
        (
            'tur123',
            'verygood@mail.ru',
            '123',
            'http://users.bugred.ru/',
            'Корректные данные'
        ),

        (
            'tur123',
            'verygoodmail.ru',
            '123',
            'http://users.bugred.ru/user/register/index.html',
            'Пропуск @ в email'
        ),

        (
            'tur123',
            'verygood@mailru',
            '123',
            'http://users.bugred.ru/user/register/index.html',
            'Пропуск . в email'
        ),

        (
            '',
            'verygood@mail.ru',
            '123',
            'http://users.bugred.ru/user/login/index.html',
            'Пропуск имени пользователя'
        ),

        (
            'tur123',
            '',
            '123',
            'http://users.bugred.ru/user/login/index.html',
            'Пропуск email пользователя'
        ),
        
        (
            'tur123',
            'verygood@mail.ru',
            '',
            'http://users.bugred.ru/user/login/index.html',
            'Пропуск пароля пользователя'
        ),
    ]

    def __registration_page(self, driver, first_name, email, password) -> None:
        from_page = RegistrationPage(driver, 'http://users.bugred.ru/user/login/index.html')
        from_page.open()
        from_page.registration_and_submit(first_name, email, password)

    def __logout(self, driver):
        from_page = LogoutPage(driver, 'http://users.bugred.ru/user/login/index.html')
        from_page.open()
        from_page.logout()

    def __delete_user(self, driver):
        email = 'manager@mail.ru'
        password = '1'
        user_name_delete = 'tur123'

        from_page = DeletePage(driver, 'http://users.bugred.ru/user/login/index.html')
        from_page.open()
        from_page.delete_user(email, password, user_name_delete)

    @pytest.mark.parametrize('test_data', __test_data)
    def test_user_registration_positive(self, screenshot, driver, test_data):
        first_name, email, password, expected_result, title_test = test_data
        allure.dynamic.title(f"{title_test}")
        with allure.step(title_test):
            self.__registration_page(driver, first_name, email, password)
        result = driver.current_url

        if result == 'http://users.bugred.ru/':
            with allure.step('Выход из под зарегистрированного пользователя'):
                self.__logout(driver)
            with allure.step('Авторизация и удаление пользователя из под админки'):
                self.__delete_user(driver)
            with allure.step('Выход из под админестратора'):
                self.__logout(driver)

        assert expected_result == result, 'Ошибка при регистрации пользователя'