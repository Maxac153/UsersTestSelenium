import pytest
from pages.profile_page import ProfilePage


class TestAddAvatar:
    __test_data = [
        ('manager@mail.ru',
         '1',
         '/home/turgor/PycharmProjects/UsersTestSelenium/img/img_8Kb.png',
         'http://users.bugred.ru/tmp/default_avatar.jpg'),

        ('manager@mail.ru',
         '1',
         '/home/turgor/PycharmProjects/UsersTestSelenium/img/img_8Kb.png',
         'http://users.bugred.ru/tmp/default_avatar.jpg')
    ]

    def __profile_page(slef, driver, email, password, img):
        from_page = ProfilePage(driver, 'http://users.bugred.ru/user/login/index.html')
        from_page.open()
        result = from_page.authorization(email, password, img)
        return result

    @pytest.mark.parametrize('test_data', __test_data)
    def test_user_add_avatar(self, driver, test_data):
        email, password, img, expected_result = test_data
        result = self.__profile_page(driver, email, password, img)
        assert not expected_result == result
