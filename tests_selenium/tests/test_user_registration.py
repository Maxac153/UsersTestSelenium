import pytest
import allure

from tests_selenium.pages.authorization_and_registration_page import AuthorizationAndRegistrationPage


@allure.epic('Проверка регистрации')
class TestUserRegistration:
    URL = 'http://users.bugred.ru/user/login/index.html'
    test_data = [
        (
            'Корректные данные',
            'tur123',
            'verygood@mail.ru',
            '123',
            'http://users.bugred.ru/'
        ),

        (
            'Пропуск @ в email',
            'tur123',
            'verygoodmail.ru',
            '123',
            'http://users.bugred.ru/user/register/index.html'
        ),

        (
            'Пропуск . в email',
            'tur123',
            'verygood@mailru',
            '123',
            'http://users.bugred.ru/user/register/index.html'
        ),

        (
            'Пропуск имени пользователя',
            '',
            'verygood@mail.ru',
            '123',
            'http://users.bugred.ru/user/login/index.html'
        ),

        (
            'Пропуск email пользователя',
            'tur123',
            '',
            '123',
            'http://users.bugred.ru/user/login/index.html'
        ),

        (
            'Пропуск пароля пользователя',
            'tur123',
            'verygood@mail.ru',
            '',
            'http://users.bugred.ru/user/login/index.html'
        ),
    ]

    @pytest.mark.parametrize('test_data', test_data)
    def test_user_registration_positive(self, screenshot, driver, test_data):
        with allure.step('Подготовка данных'):
            test_name, user_name, email, password, expected_result = test_data
            allure.dynamic.title(test_name)

        with allure.step('Регистрация пользователя'):
            aut_reg_page = AuthorizationAndRegistrationPage(driver, self.URL)
            aut_reg_page.open()

            with allure.step('Ввод данных и регистрация'):
                aut_reg_page.registration(user_name, email, password)
                result = driver.current_url

            if result == 'http://users.bugred.ru/':
                with allure.step('Удаление пользователя (если успешная регистрация)'):
                    aut_reg_page.logout_account()
                    aut_reg_page.open()
                    aut_reg_page.authorization('manager@mail.ru', '1')
                    aut_reg_page.delete_user_account(user_name)
                    aut_reg_page.logout_account()

            with allure.step('Проверка результата'):
                assert expected_result == result, 'Ошибка при регистрации пользователя'
