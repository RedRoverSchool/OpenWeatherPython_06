import jsonschema
import requests
import json
from os.path import join, dirname
from jsonschema import Draft202012Validator

# End points
BASE_PAGE = 'https://reqres.in'
SINGLE_USER = '/api/users/2'
LIST_USERS = '/api/users?page=2'


def validator(data, schema_file):
    """ Checks whether the given data matches the schema.
        Also checks if schema is valid.
    """
    schema = _load_json_schema(schema_file)
    try:
        Draft202012Validator.check_schema(schema)
    except jsonschema.exceptions.SchemaError as e:
        print("JSON Schema is incorrect:", e)
    else:
        return Draft202012Validator(schema).is_valid(data)


def _load_json_schema(filename):
    """ Loads the given schema file """

    relative_path = join('schemas', filename)
    absolute_path = join(dirname(__file__), relative_path)
    try:
        with open(absolute_path) as schema_file:
            try:
                return json.loads(schema_file.read())
            except json.decoder.JSONDecodeError:
                print(f"JSON file has incorrect data: {relative_path}")
    except FileNotFoundError:
        print(f"No such JSON schema file: {relative_path}")
        return False


# Tests
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
