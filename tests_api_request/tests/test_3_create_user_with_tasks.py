import requests

def test_create_user_with_tasks():
    url = "http://users.bugred.ru/tasks/rest/createuserwithtasks"

    data = {
        "email": "fsje@gmail.com",
        "name": "serg",
        "tasks": [{
            "title": "Задача №2",
            "description": "Что-то сделать"
        }]
    }

    response = requests.post(url, json=data)
    assert response.status_code == 200
    assert response.json()['name'] == 'serg'
    assert response.json()['email'] == 'fsje@gmail.com'
    assert response.json()['by_user'] == 'manager@mail.ru'
