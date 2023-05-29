from pages.base_page import BasePage
from tests.test_group_100000.locators.api_page_locators import RoadRiskApi as R
from tests.test_group_100000.locators.api_page_locators import WeatherConditions as W

class RoadRiskApi(BasePage):
    def check_redirect_to_page_section(self):
        self.driver.find_element(*R.LINK_HOW_TO_REQUEST_RR_API).click()
        section_title = self.driver.find_element(*R.TITLE_HOW_TO_RR_API)
        assert section_title.is_displayed(), 'Title Not Found'

    def check_visibility_concept_section(self):
        section_road_risk = self.driver.find_element(*R.SECTION_R_CONCEPTS)
        assert section_road_risk.is_displayed(), 'Section - NOT FOUND'

    def check_module_title_road_risk_page(self):
        expected_title = 'Road Risk API'
        title_module = self.driver.find_element(*R.TITLE_ROAD_RISK)
        assert expected_title in title_module.text, 'Title Not Found'


class WeatherConditionsPage(BasePage):
    def check_visibility_drizzle_group(self):
        drizzle_codes = self.driver.find_element(*W.DRIZZLE_LOCATOR)
        assert drizzle_codes.is_displayed()