from api_testing.utils.file_handler import FileHandler
from api_testing.pages.file_handler_page import FileHandlerPage


class TestRequestHandler:
    file_handler = FileHandler()
    file_handler_page = FileHandlerPage()

    def test_request_response_as_data_source(self):
        data_source = self.file_handler_page.get_data_source().json()
        file_path = self.file_handler_page.path_json_file()
        self.file_handler.write_into_json_file(data_source, file_path)
        data_from_file = self.file_handler.read_from_json_file(file_path)
        assert data_source == data_from_file, "Data from request is not equal to data from JSON file"
