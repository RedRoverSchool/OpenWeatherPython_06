from pages.base_page import BasePage
from tests.group_files.group_future_auto_qa.locators.api_page_locators import ApiPageLocators


class ApiPage(BasePage):
    locators = ApiPageLocators()

    def check_page_title(self, page_title):
        api_page = ApiPage(self.driver, "https://openweathermap.org/api")
        api_page.open_page()
        assert self.driver.title == page_title, "The title of the page is incorrect"

