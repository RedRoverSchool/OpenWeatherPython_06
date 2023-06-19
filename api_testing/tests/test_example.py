from pprint import pprint
import logging
from api_testing.utils.http_handler import HTTPHandler
from api_testing.utils.logger import setup_logging

logger = logging.getLogger("api_testing.test_get_all_users")

def test_example():
    url = "/api/users/2"
    response = HTTPHandler.get(url)
    pprint(response)
    logger.info("")


def test_post_create():
    url = "/api/users"
    data = {
        "name": "morpheus",
        "job": "leader"
    }
    response = HTTPHandler.post(url, data)
    print(response.json())
    logger.info("Get logs v.2")