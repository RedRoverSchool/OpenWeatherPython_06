import requests

def test_get_all_users():
    response = requests.get('https://reqres.in/api/users')
    assert response.status_code == 200