import allure
import pytest

from pages.logout_page import LogoutPage
from pages.profile_page import ProfilePage


@allure.epic('Проверка изменения аватара пользователя')
class TestAddAvatar:
    __test_data = [
        (
            'manager@mail.ru',
            '1',
            '/home/turgor/PycharmProjects/UsersTestSelenium/img/img_8Kb.png',
            True,
            'Размер аватарки меньше 150Kb'
        ),

        (
            'manager@mail.ru',
            '1',
            '/home/turgor/PycharmProjects/UsersTestSelenium/img/img_more_150Kb.jpg',
            False,
            'Размер аватарки больше 150Kb'
        )
    ]

    def __profile_page(slef, driver, email, password, img):
        from_page = ProfilePage(driver, 'http://users.bugred.ru/user/login/index.html')
        from_page.open()
        result = from_page.authorization(email, password, img)
        return result

    @pytest.mark.parametrize('test_data', __test_data)
    def test_user_add_avatar(self, logout, screenshot, driver, test_data):
        email, password, img, expected_result, title_test = test_data
        allure.dynamic.title(f"{title_test}")
        with allure.step('Изменение аватара пользователя'):
            result = self.__profile_page(driver, email, password, img)
        assert expected_result == result.split('/')[-1].isdigit(), 'Ошибка добавления аватарки некорректный размер'
