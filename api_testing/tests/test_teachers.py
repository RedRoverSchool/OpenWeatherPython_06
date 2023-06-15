import logging
import requests
from api_testing.utils.logger import setup_logging

logger = logging.getLogger("api_testing.test_get_all_users")


def test_get_all_users():
    try:
        response = requests.get('https://reqres.in/api/users')
        assert response.status_code == 203
        logger.info("completed successfully")
    except AssertionError as e:
        error_message = f"Test assertion failed: {str(e)}"
        logger.error(error_message)
        raise AssertionError(error_message)
