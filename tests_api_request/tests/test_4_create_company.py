import requests

def test_create_company():
    url = "http://users.bugred.ru/tasks/rest/createcompany"

    data = {
        "company_name": "KJSkdfjlsdjf",
        "company_type": "ОАО",
        "company_users[0]": "verygood@mail.ru",
        "email_owner": "verygood@mail.ru"
    }

    response = requests.post(url, json=data)
    assert response.status_code == 200