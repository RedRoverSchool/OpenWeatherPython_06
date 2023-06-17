from api_testing.utils.handlers.http_handler import HTTPHandler

# End points
SINGLE_USER = '/api/users/2'

class Tests:

    def test_get_single_user_schemas(self):
        get_single_user = HTTPHandler.get(SINGLE_USER, 'single_user.json')
        print('\n', get_single_user)
        assert get_single_user, 'API response is incorrect'
