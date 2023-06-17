from api_testing.utils.handlers.http_handler import HTTPHandler

# End points
LIST_USERS = 'api/users?page=2'
CREATE_POST = 'api/users'
PUT_UPDATE = 'api/users/2'
PATCH_UPDATE = 'api/users/2'
DELETE_USER_2 = 'api/users/2'
SINGLE_USER = '/api/users/2'

class Tests:

    def test_user_get(self):
        handler = HTTPHandler()
        response_get = handler.get(LIST_USERS)
        print('response_get: ', response_get)
        assert response_get['total'] == 12, 'API response is incorrect'

    def test_create_post(self):
        handler = HTTPHandler()
        post_create_data = {"name": "morpheus", "job": "leader"}
        response_get = handler.post(CREATE_POST, post_create_data)
        print('response_get: ', response_get)
        assert response_get['name'] == 'morpheus' and response_get['job'] == 'leader', 'API response is incorrect'

    def test_put_update(self):
        handler = HTTPHandler()
        data = {"name": "morpheus", "job": "friend of neo"}
        response_get = handler.put(PUT_UPDATE, data)
        print('response_get: ', response_get)
        assert response_get['name'] == 'morpheus' and response_get['job'] == 'friend of neo', 'API response is incorrect'

    def test_patch_update(self):
        handler = HTTPHandler()
        data = {"name": "trinity", "job": "friend of neo"}
        response_get = handler.patch(PATCH_UPDATE, data)
        print('response_get: ', response_get)
        assert response_get['name'] == 'trinity' and response_get['job'] == 'friend of neo', 'API response is incorrect'

    def test_delete_update(self):
        handler = HTTPHandler()
        post_create_data = {"name": "morpheus", "job": "leader"}
        response_create = handler.post(CREATE_POST, post_create_data)
        print('\nresponse_create: ', response_create)
        response_delete = handler.delete(DELETE_USER_2)
        print('response_get.status_code: ', response_delete)
        assert response_delete == 204, 'API response is incorrect'

    def test_get_single_user_schemas(self):
        get_single_user = HTTPHandler.get(SINGLE_USER, 'single_user.json')
        print('\n', get_single_user)
        assert get_single_user, 'API response is incorrect'

    def test_post_single_user_schemas(self):
        handler = HTTPHandler()
        post_create_data = {"name": "morpheus", "job": "leader"}
        response_get = handler.post(CREATE_POST, post_create_data)
        print('response_get: ', response_get)
        assert response_get['name'] == 'morpheus' and response_get['job'] == 'leader', 'API response is incorrect'
