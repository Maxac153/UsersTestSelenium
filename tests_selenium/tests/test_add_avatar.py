import os

import allure
import pytest

from tests_selenium.pages.authorization_and_registration_page import AuthorizationAndRegistrationPage
from tests_selenium.pages.profile_page import ProfilePage


@allure.epic('Проверка изменения аватара пользователя')
class TestAddAvatar:
    URL = 'http://users.bugred.ru/user/login/index.html'
    test_data = [
        (
            'Размер аватарки меньше 150Kb',
            'manager@mail.ru',
            '1',
            os.path.abspath('tests_selenium/resources/img/img_8Kb.png'),
            True

        ),

        (
            'Размер аватарки больше 150Kb',
            'manager@mail.ru',
            '1',
            os.path.abspath('tests_selenium/resources/img/img_more_150Kb.png'),
            False
        )
    ]

    @pytest.mark.parametrize('test_data', test_data)
    def test_user_add_avatar(self, screenshot, driver, test_data: list):
        with allure.step('Подготовка данных'):
            test_name, email, password, img, expected_result = test_data
            allure.dynamic.title(test_name)

        with allure.step('Изменение аватара пользователя'):
            aut_reg_page = AuthorizationAndRegistrationPage(driver, self.URL)
            aut_reg_page.open()
            with allure.step('Авторизация'):
                aut_reg_page.authorization(email, password)
                aut_reg_page.into_user_account()

            with allure.step('Загрузка картинки'):
                profile_page = ProfilePage(driver)
                result = profile_page.replace_avatar(img)
                profile_page.logout_account()

            with allure.step('Проверка результата'):
                assert expected_result == result.split('/')[-1].isdigit(), 'Ошибка добавления аватарки некорректный размер'
