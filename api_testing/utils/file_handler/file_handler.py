import json


class FileHandler:
    def write_into_json_file(self, data, file_path):
        with open(file_path, 'w') as file:
            json.dump(data, file)

    def read_from_json_file(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
