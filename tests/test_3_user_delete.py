import pytest
from pages.delete_page import DeletePage

@pytest.mark.run(order=1)
def test_user_delete(driver):
    email = 'manager@mail.ru'
    password = '1'
    user_name_delete = 'tur123'

    from_page = DeletePage(driver, 'http://users.bugred.ru/user/login/index.html')
    from_page.open()
    result = from_page.delete_user(email, password, user_name_delete)
    expected_result = 'Всего:0 '
    assert result == expected_result