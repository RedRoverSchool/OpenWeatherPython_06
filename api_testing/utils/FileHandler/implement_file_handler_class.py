import json
import requests


class FileHandler:
    def write_into_json_file(self, data, filename):
        with open(filename, 'w') as file:
            json.dump(data, file)

    def read_from_json_file(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return data


class TestRequestHandler(FileHandler):
    def test_request_response_as_data_source(self):
        url = 'https://reqres.in/api/users?page=2'
        response = requests.get(url)
        data_from_request = response.json()
        filename = 'data_from_request_response.json'
        FileHandler.write_into_json_file(self, data_from_request, filename)
        data_from_file = FileHandler.read_from_json_file(self, filename)
        assert data_from_request == data_from_file, "Data from request is not equal to data from JSON file"
