import pytest

from pages.delete_page import DeletePage
from pages.logout_page import LogoutPage
from pages.registration_page import RegistrationPage

class TestUserRegistration:
    data = [
        ('tur123', 'verygood@mail.ru', '123', 'http://users.bugred.ru/'),
        ('tur123', 'verygoodmail.ru', '123', 'http://users.bugred.ru/user/register/index.html'),
        ('tur123', 'verygood@mailru', '123', 'http://users.bugred.ru/user/register/index.html'),
        ('', 'verygood@mail.ru', '123', 'http://users.bugred.ru/user/login/index.html'),
        ('tur123', '', '123', 'http://users.bugred.ru/user/login/index.html'),
        ('tur123', 'verygood@mail.ru', '', 'http://users.bugred.ru/user/login/index.html'),
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

    @pytest.mark.parametrize('data', data)
    def test_user_registration_positive(self, driver, data):
        first_name, email, password, expected_result = data
        self.__registration_page(driver, first_name, email, password)
        result = driver.current_url

        if result == 'http://users.bugred.ru/':
            self.__logout(driver)
            self.__delete_user(driver)
            self.__logout(driver)

        assert expected_result == result, 'Ошибка при регистрации пользователя'
