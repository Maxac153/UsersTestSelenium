import pytest
from pages.authorization_page import AuthorizationPage

@pytest.mark.run(order=1)
def test_user_authorization(driver):
    email = 'verygood@mail.ru'
    password = '123'

    from_page = AuthorizationPage(driver, 'http://users.bugred.ru/user/login/index.html')
    from_page.open()
    result = from_page.authorization(email, password)
    expected_result = 'tur123'
    assert expected_result == result

@pytest.mark.run(order=2)
def test_manager_authorization(driver):
    email = 'manager@mail.ru'
    password = '1'

    from_page = AuthorizationPage(driver, 'http://users.bugred.ru/user/login/index.html')
    from_page.open()
    result = from_page.authorization(email, password)
    expected_result = 'Злобный босс'
    assert expected_result == result