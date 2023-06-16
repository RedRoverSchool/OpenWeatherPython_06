import requests
import json
from api_testing.utils.validator import validator

class HTTPHandler:
    BASE_URL = "https://reqres.in"

    @staticmethod
    def validate_response(response):
        try:
            response_json = response.json()
            is_valid = validator(response_json, "list_users.json")
            if not is_valid:
                raise Exception("Invalid JSON response")
        except json.JSONDecodeError:
            raise Exception("Invalid JSON response:", json.JSONDecodeError)

    @classmethod
    def get(cls, endpoint):
        url = f"{cls.BASE_URL}/{endpoint}"
        response = requests.get(url)
        cls.validate_response(response)
        return response.json()

    @classmethod
    def post(cls, endpoint, data):
        url = f"{cls.BASE_URL}/{endpoint}"
        response = requests.post(url, json=data)
        cls.validate_response(response)
        return response.json()

    @classmethod
    def put(cls, endpoint, data):
        url = f"{cls.BASE_URL}/{endpoint}"
        response = requests.put(url, json=data)
        cls.validate_response(response)
        return response.json()

    @classmethod
    def patch(cls, endpoint, data):
        url = f"{cls.BASE_URL}/{endpoint}"
        response = requests.patch(url, json=data)
        cls.validate_response(response)
        return response.json()

    @classmethod
    def delete(cls, endpoint):
        url = f"{cls.BASE_URL}/{endpoint}"
        response = requests.delete(url)
        # response_json = response.json()
        # cls.validate_response(response)
        return response.status_code
