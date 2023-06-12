import pytest
from pages.profile_page import ProfilePage

def test_user_add_avatar_less_150Kb(driver):
    email = 'manager@mail.ru'
    password = '1'
    img = "/home/turgor/PycharmProjects/UsersTestSelemium/img/img_8Kb.png"

    from_page = ProfilePage(driver, 'http://users.bugred.ru/user/login/index.html')
    from_page.open()
    result = from_page.authorization(email, password, img)

    assert not 'http://users.bugred.ru/tmp/default_avatar.jpg' == result

def test_user_add_avatar_more_150Kb(driver):
    email = 'manager@mail.ru'
    password = '1'
    img = "/home/turgor/PycharmProjects/UsersTestSelemium/img/img_more_150Kb.jpg"

    from_page = ProfilePage(driver, 'http://users.bugred.ru/user/login/index.html')
    from_page.open()
    result = from_page.authorization(email, password, img)

    assert 'http://users.bugred.ru/tmp/default_avatar.jpg' == result, \
        "Некорректный размер картинки (файл привышает лимит по размеру > 150Kb)!"