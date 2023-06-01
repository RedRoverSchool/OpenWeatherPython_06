from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from tests.test_group_100000.locators.api_page_locators import RoadRiskApi as R
from tests.test_group_100000.locators.api_page_locators import WeatherConditions as W
from tests.test_group_100000.locators.api_page_locators import OneCallApi as O


class RoadRiskApi(BasePage):
    page_loc = R

    def open_road_risk_api_page(self):
        self.driver.get(R.ROAD_RISK_API_LINK)

    def check_redirect_to_page_section(self):
        self.open_road_risk_api_page()
        self.driver.find_element(*R.LINK_HOW_TO_REQUEST_RR_API).click()
        section_title = self.driver.find_element(*R.TITLE_HOW_TO_RR_API)
        assert section_title.is_displayed(), 'Title Not Found'

    def check_visibility_concept_section(self):
        self.open_road_risk_api_page()
        section_road_risk = self.driver.find_element(*R.SECTION_R_CONCEPTS)
        assert section_road_risk.is_displayed(), 'Section - NOT FOUND'

    def check_module_title_road_risk_page(self):
        self.open_road_risk_api_page()
        expected_title = 'Road Risk API'
        title_module = self.driver.find_element(*R.TITLE_ROAD_RISK)
        assert expected_title in title_module.text, 'Title Not Found'

    def check_redirection_to_the_section_of_the_page(self):
        self.open_road_risk_api_page()
        self.driver.find_element(*R.LINK_LIST_OF_NATIONAL).click()
        assert self.element_is_visible(self.page_loc.TITLE_LIST_OF_NATIONAL).text == "List of national " \
                                                                                     "weather warning sources"

    def verify_redirection_to_the_page_with_api_keys(self):
        self.open_road_risk_api_page()
        self.allow_all_cookies()
        self.driver.find_element(*R.LINK_API_KEY_TAB).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert self.element_is_visible(self.page_loc.LIST_API_KEYS)

    def verification_sources_list(self):
        self.open_road_risk_api_page()
        self.driver.find_element(*R.LINK_LIST_OF_NATIONAL).click()
        self.allow_all_cookies()
        list_sours = self.driver.find_element(*R.BLOCK_LIST_SOURCE)
        rows = list_sours.find_elements(By.TAG_NAME, 'tr')
        for row in rows[1:]:
            cells = row.find_elements(By.TAG_NAME, 'td')
            for cell in cells:
                if cell.text.strip():
                    assert cell.text.strip(), 'Value not found'


class WeatherConditionsPage(BasePage):
    def check_visibility_drizzle_group(self):
        drizzle_codes = self.driver.find_element(*W.DRIZZLE_LOCATOR)
        assert drizzle_codes.is_displayed()


class OneCallApiPage(BasePage):
    def verify_redirection_one_call_api_3_link(self):
        self.driver.get(O.API_PAGE)
        self.driver.find_element(*O.ONE_CALL_API_3).click()
        # self.allow_all_cookies()
        expected_link = O.ONE_CALL_API_LINK
        assert self.driver.current_url == expected_link, "This link is not correct"

        # self.driver.switch_to.window(self.driver.window_handles[1])
        # button_url = self.driver.current_url
        # assert button_url == expected_link, " button link is not correct"



