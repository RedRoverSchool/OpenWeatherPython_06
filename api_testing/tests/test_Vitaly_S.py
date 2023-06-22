import allure
import pytest
from api_testing.utils.http_handler import HTTPHandler
from api_testing.utils.validator_pydantic import validator_pydantic
from api_testing.utils.models.pydantic_models import Models as m
from api_testing.data.endpoints import EndPoints as ep


@pytest.mark.positive
class Tests:
    """Positive tests with correct JSON data from endpoint and correct model"""

    @pytest.mark.response_status
    @allure.title("Get API response for 'LIST USERS' and check response status")
    def test_list_users_response_status(self):
        """Check correct response status"""
        response = HTTPHandler.get(ep.LIST_USERS)
        response_status = response.status_code
        assert response_status == 200, 'Response status code is incorrect'

    @pytest.mark.json_validation
    @allure.title("Get API response for 'LIST USERS' and validate JSON using pydentic validator")
    def test_list_users_json_validation(self):
        """Validate JSON using pydentic validator"""
        response = HTTPHandler.get(ep.LIST_USERS)
        json_data = response.json()
        assert validator_pydantic(json_data, m.ListUsers.Model), 'JSON from API response is incorrect'

    @pytest.mark.response_status
    @pytest.mark.parametrize('user', range(1, 13))
    @allure.title("Get API response for 'SINGLE USER' and check response status")
    def test_single_user_response_status(self, user):
        """Check correct response status for users from 1 to 12"""
        response = HTTPHandler.get(f'{ep.SINGLE_USER}{user}')
        response_status = response.status_code
        assert response_status == 200, 'Response status code is incorrect'

    @pytest.mark.json_validation
    @pytest.mark.parametrize('user', range(1, 13))
    @allure.title("Get API response for 'SINGLE USER' and validate JSON using pydentic validator")
    def test_single_user_json_validation(self, user):
        """Validate JSON using pydentic validator for users from 1 to 12"""
        response = HTTPHandler.get(f'{ep.SINGLE_USER}{user}')
        json_data = response.json()
        assert validator_pydantic(json_data, m.SingleUser.Model), 'JSON from API response is incorrect'

