import requests
import json
from api_testing.utils.validator import validator
import os

class HTTPHandler:
    BASE_URL = "https://reqres.in"

    @staticmethod
    def validate_response(response, schemas):
        try:
            response_json = response.json()
            is_valid = validator(response_json, schemas)  # schemas == "list_users.json" etc
            if not is_valid:
                raise Exception("Invalid JSON response")
        except json.JSONDecodeError:
            raise Exception("Invalid JSON response:", json.JSONDecodeError)

    @classmethod
    def get(cls, endpoint, schemas):
        schemas_path_and_name = os.path.join('..', 'utils', 'schemas', schemas)
        absolute_schemas_path_and_name = os.path.abspath(schemas_path_and_name)
        url = f"{cls.BASE_URL}{endpoint}"
        response = requests.get(url)
        cls.validate_response(response, absolute_schemas_path_and_name)
        return response.json()

    @classmethod
    def post(cls, endpoint, data, schemas):
        schemas_path_and_name = os.path.join('..', 'utils', 'schemas', schemas)
        absolute_schemas_path_and_name = os.path.abspath(schemas_path_and_name)
        url = f"{cls.BASE_URL}{endpoint}"
        response = requests.post(url, json=data)
        cls.validate_response(response, absolute_schemas_path_and_name)
        return response.json()

    @classmethod
    def put(cls, endpoint, data, schemas):
        schemas_path_and_name = os.path.join('..', 'utils', 'schemas', schemas)
        absolute_schemas_path_and_name = os.path.abspath(schemas_path_and_name)
        url = f"{cls.BASE_URL}{endpoint}"
        response = requests.put(url, json=data)
        cls.validate_response(response, absolute_schemas_path_and_name)
        return response.json()

    @classmethod
    def patch(cls, endpoint, data, schemas):
        schemas_path_and_name = os.path.join('..', 'utils', 'schemas', schemas)
        absolute_schemas_path_and_name = os.path.abspath(schemas_path_and_name)
        url = f"{cls.BASE_URL}{endpoint}"
        response = requests.patch(url, json=data)
        cls.validate_response(response, absolute_schemas_path_and_name)
        return response.json()

    @classmethod
    def delete(cls, endpoint):
        url = f"{cls.BASE_URL}{endpoint}"
        response = requests.delete(url)
        return response.status_code
