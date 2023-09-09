import requests

def test_create_user():
    url = "http://users.bugred.ru/tasks/rest/createcompany"

    data = {
        "email": "fskdje@gmail.com",
        "name": "serwdg",
        "tasks[0]": "56",
        "companies[0]": "39"
    }

    response = requests.post(url, json=data)
    assert response.status_code == 200