import requests

def test_user_registration_with_correct_data(delete_user):
    url = "http://users.bugred.ru/tasks/rest/doregister"

    data = {
        "email": "verygood@mail.ru",
        "name": "Tur123",
        "password": "123"
    }

    response = requests.post(url, json=data)
    assert response.status_code == 200
    assert response.json()['name'] == 'Tur123'
    assert response.json()['avatar'] == 'http://users.bugred.ru//tmp/default_avatar.jpg'
    assert response.json()['birthday'] == 0
    assert response.json()['email'] == 'verygood@mail.ru'
    assert response.json()['gender'] == ''
    assert response.json()['date_start'] == 0
    assert response.json()['hobby'] == ''

def test_user_registration_skipping_name():
    url = "http://users.bugred.ru/tasks/rest/doregister"

    data = {
        "email": "verygood@mail.ru",
        "name": "",
        "password": "123"
    }

    response = requests.post(url, json=data)
    assert response.status_code == 200
    assert response.json()['type'] == 'error'
    assert response.json()['message'] == 'поле фио является обязательным'

def test_user_registration_skipping_password():
    url = "http://users.bugred.ru/tasks/rest/doregister"

    data = {
        "email": "verygood@mail.ru",
        "name": "Tur123",
        "password": ""
    }

    response = requests.post(url, json=data)
    assert response.status_code == 200
    assert response.json()['type'] == 'error'
    assert response.json()['message'] == 'поле пароль является обязательным'
    
def test_user_registration_skipping_email():
    url = "http://users.bugred.ru/tasks/rest/doregister"

    data = {
        "email": "",
        "name": "Tur123",
        "password": "123"
    }

    response = requests.post(url, json=data)
    assert response.status_code == 200
    assert response.json()['type'] == 'error'
    assert response.json()['message'] == ' Некоректный  email '
def test_user_registration_skipping_the_at_symbol_in_email():
    url = "http://users.bugred.ru/tasks/rest/doregister"

    data = {
        "email": "verygoodmail.ru",
        "name": "Tur123",
        "password": "123"
    }

    response = requests.post(url, json=data)
    assert response.status_code == 200
    assert response.json()['type'] == 'error'
    assert response.json()['message'] == ' Некоректный  email verygoodmail.ru'

def test_user_registration_skipping_the_point_symbol_in_email():
    url = "http://users.bugred.ru/tasks/rest/doregister"

    data = {
        "email": "verygood@mailru",
        "name": "Tur123",
        "password": "123"
    }

    response = requests.post(url, json=data)
    assert response.status_code == 200
    assert response.json()['type'] == 'error'
    assert response.json()['message'] == ' Некоректный  email verygood@mailru'