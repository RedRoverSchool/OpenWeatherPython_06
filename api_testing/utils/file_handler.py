import json
import allure


class FileHandler:
    @allure.step("This method writes data into json files")
    def write_into_json_file(self, data, file_path):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    @allure.step("This method reads data from json files")
    def read_from_json_file(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
