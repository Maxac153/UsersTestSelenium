import requests

def test_magic_search():
    url = "http://users.bugred.ru/tasks/rest/magicsearch?query=Tur123"

    response = requests.get(url)
    assert response.status_code == 231
    assert response.json()['foundCount'] == 1
