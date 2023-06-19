from api_testing.utils.file_handler import FileHandler
import requests
import os


class TestRequestHandler:
    file_handler = FileHandler()

    def test_request_response_as_data_source(self):
        url = 'https://reqres.in/api/users?page=2'
        response = requests.get(url)
        data_from_request = response.json()
        file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'data_from_request_response.json')
        self.file_handler.write_into_json_file(data_from_request, file_path)
        data_from_file = self.file_handler.read_from_json_file(file_path)
        assert data_from_request == data_from_file, "Data from request is not equal to data from JSON file"
