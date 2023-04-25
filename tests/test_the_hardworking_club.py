import requests
import pytest

BASE_URL = 'https://restful-booker.herokuapp.com/booking'
AUTH_URL = 'https://restful-booker.herokuapp.com/auth'


STATUS_OK = 200

@pytest.fixture(scope='module')
def auth_token():
    payload = {
            "username": "admin",
            "password": "password123"
    }
    response = requests.post(AUTH_URL, json=payload)
    response_data = response.json()
    token = response_data['token']
    assert response.status_code == STATUS_OK
    yield token


@pytest.fixture(scope='module')
def booking_id():
    payload = {
        "firstname": "John",
        "lastname": "Smith",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(BASE_URL, json=payload)
    booking_id = response.json()['bookingid']
    assert response.status_code == 200
    yield booking_id



def test_get_all_booking():
    response = requests.get(BASE_URL)
    # print(response.status_code)
    assert response.status_code == 200

    print(len(response.headers))

    print(f'{response.headers}')
    print(response.json())

    headers = {'Connection', 'keep-alive'}
    assert headers in response.headers.items()

    print(f'\n{len(response.json())}')

    key = 'Connection'
    assert key in response.headers


