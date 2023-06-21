import allure
import requests
import os


class FileHandlerPage:
    @allure.step("This method initializes a path for JSON file")
    def path_json_file(self):
        file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'data_from_request_response.json')
        return file_path

    @allure.step("This method use request response as data source")
    def get_data_source(self):
        url = 'https://reqres.in/api/users?page=2'
        data_source = requests.get(url)
        return data_source
