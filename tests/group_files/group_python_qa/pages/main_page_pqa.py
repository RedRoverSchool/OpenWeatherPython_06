from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from tests.group_files.group_python_qa.locators.locators import MainPageLocators


class MainPage(BasePage):

    locator = MainPageLocators()

    def fill_city_search_field(self, city):
        input_city = self.driver.find_element(*self.locator.SEARCH_CITY_FIELD_LOCATOR)
        input_city.send_keys(city)

    def click_search_button(self):
        self.driver.find_element(*self.locator.SEARCH_BUTTON_LOCATOR).click()

    def choose_1st_option(self, wait):
        wait.until(EC.element_to_be_clickable(self.locator.SEARCH_1ST_OPTION_LOCATOR)).click()

    def switch_to_c_temp(self):
        self.driver.find_element(*self.locator.C_TEMP_LOCATOR).click()

    def check_8_lines_are_displayed(self):
        lines = self.driver.find_elements(*self.locator.LINE_IN_8_DAYS_FORECAST_LOCATOR)
        for line in lines:
            assert line.is_displayed()

    def visibility_of_agriculture_analytics_link(self):
        self.driver.find_element(*self.locator.AGRICULTURE_ANALYTICS_TITLE_LOCATOR).is_displayed()


    def visibility_of_nwp_block(self):
        nwp = self.driver.find_element(*self.locator.NWP_MODEL)
        assert nwp.is_displayed()


