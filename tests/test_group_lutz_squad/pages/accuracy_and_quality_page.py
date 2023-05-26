from pages.base_page import BasePage
from tests.test_group_lutz_squad.locators.accuracy_and_quality_page_locators import AccuracyAndQualityPageLocators as AC


class AccuracyAndQualityPage(BasePage):
    def check_visibility_of_number_of_cities(self):
        number_of_cities = self.driver.find_element(*AC.number_of_cities_for_evaluation)
        assert number_of_cities.is_displayed(), 'Number of cities link not found'
