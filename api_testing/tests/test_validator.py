import requests
from api_testing.utils.validator import validator

# End points
BASE_PAGE = 'https://reqres.in'
SINGLE_USER = '/api/users/2'
LIST_USERS = '/api/users?page=2'


class Tests:

    def test_single_user(self):
        response = requests.get(f'{BASE_PAGE}{SINGLE_USER}')
        json_data = response.json()
        print(json_data)
        assert validator(json_data, 'single_user.json'), 'API response is incorrect'

    def test_list_users(self):
        response = requests.get(f'{BASE_PAGE}{LIST_USERS}')
        json_data = response.json()
        print(json_data)
        assert validator(json_data, 'list_users.json'), 'API response is incorrect'
