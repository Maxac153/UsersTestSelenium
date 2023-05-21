import pytest
from pages.profile_page import ProfilePage

@pytest.mark.run(order=1)
def test_user_authorization(driver):
    email = 'verygood@mail.ru'
    password = '123'

    from_page = ProfilePage(driver, 'http://users.bugred.ru/user/login/index.html')
    from_page.open()
    result = from_page.authorization(email, password)


    assert  not 'http://users.bugred.ru/tmp/default_avatar.jpg' == result