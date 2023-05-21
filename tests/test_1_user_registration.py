import pytest
from pages.registration_page import RegistrationPage

@pytest.mark.run(order=1)
def test_user_registration(driver):
    first_name = 'tur123'
    email = 'verygood@mail.ru'
    password = '123'

    from_page = RegistrationPage(driver, 'http://users.bugred.ru/user/login/index.html')
    from_page.open()
    from_page.registration_and_submit(first_name, email, password)
    result = from_page.user_authorization()
    expected_result = first_name
    assert expected_result == result

@pytest.mark.run(order=2)
def test_user_registration_already_database(driver):
    first_name = 'tur123'
    email = 'verygood@mail.ru'
    password = '123'

    from_page = RegistrationPage(driver, 'http://users.bugred.ru/user/login/index.html')
    from_page.open()
    from_page.registration_and_submit(first_name, email, password)
    result = from_page.error_message()
    expected_result = 'Занят (name)'
    assert expected_result == result

@pytest.mark.run(order=3)
def test_user_registration_skipping_the_at_symbol_in_email(driver):
    first_name = 'tur123'
    email = 'verygoodmail.ru'
    password = '123'

    from_page = RegistrationPage(driver, 'http://users.bugred.ru/user/login/index.html')
    from_page.open()
    from_page.registration_and_submit(first_name, email, password)
    result = from_page.error_message()
    expected_result = 'Неправильное значение поля (email)'
    assert expected_result == result

@pytest.mark.run(order=4)
def test_user_registration_skipping_the_point_symbol_in_email(driver):
    first_name = 'tur123'
    email = 'verygood@mailru'
    password = '123'

    from_page = RegistrationPage(driver, 'http://users.bugred.ru/user/login/index.html')
    from_page.open()
    from_page.registration_and_submit(first_name, email, password)
    result = from_page.error_message()
    expected_result = 'Неправильное значение поля (email)'
    assert expected_result == result

@pytest.mark.run(order=5)
def test_user_registration_user_4(driver):
    first_name = ''
    email = 'verygood@mail.ru'
    password = '123'

    from_page = RegistrationPage(driver, 'http://users.bugred.ru/user/login/index.html')
    from_page.open()
    result = from_page.registration_and_submit(first_name, email, password)
    expected_result = first_name
    assert expected_result == result

@pytest.mark.run(order=6)
def test_user_registration_user_5(driver):
    first_name = 'tur123'
    email = ''
    password = '123'

    from_page = RegistrationPage(driver, 'http://users.bugred.ru/user/login/index.html')
    from_page.open()
    result = from_page.registration_and_submit(first_name, email, password)
    expected_result = first_name
    assert expected_result == result

@pytest.mark.run(order=7)
def test_user_registration_user_6(driver):
    first_name = 'tur123'
    email = 'verygood@mail.ru'
    password = ''

    from_page = RegistrationPage(driver, 'http://users.bugred.ru/user/login/index.html')
    from_page.open()
    result = from_page.registration_and_submit(first_name, email, password)
    expected_result = first_name
    assert expected_result == result