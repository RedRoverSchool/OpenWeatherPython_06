from pages.base_page import BasePage
from tests.group_files.pandoras_box.pages.header import Header
from tests.group_files.pandoras_box.pages.main_page import MainPage

class MapsPage(BasePage):

    MAPS_URL = 'https://openweathermap.org/weathermap'

    def check_return_main(self):
        self.driver.find_element(*Header.logo_locator).click()
        assert self.driver.current_url == MainPage.HOME_PAGE
