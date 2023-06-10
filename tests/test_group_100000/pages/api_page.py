from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from tests.test_group_100000.locators.api_page_locators import RoadRiskApi as R, ClimateForecast
from tests.test_group_100000.locators.api_page_locators import WeatherConditions as W
from tests.test_group_100000.locators.api_page_locators import OneCallApi as O
from tests.test_group_100000.locators.main_page_locators import FooterBlockLocators as F


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
        expected_link = O.ONE_CALL_API_LINK
        assert self.driver.current_url == expected_link, "This link is not correct"


class FooterApiPage(BasePage):
    def verify_the_copyright_information_is_present_on_the_site_page(self):
        self.allow_all_cookies()
        expected_footer_text = "© 2012 — 2023 OpenWeather"
        footer = self.driver.find_element(*F.FOOTER_COPYRIGHT)
        assert footer.is_displayed() and expected_footer_text in footer.text, \
            "The footer is not displayed or does not contain the expected text"


class ClimaticForecast(BasePage):
    def check_visibility_climatic_forecast_30_days_page_title(self):
        title_page = self.driver.find_element(*ClimateForecast.TITLE_FORCAST30).text
        assert title_page == 'Climate forecast for 30 days', 'The title of the page does not match the expected value'

    def check_redirect_to_the_how_to_make_of_the_page(self):
        self.find_element_and_click(ClimateForecast.LINK_HOW_TO_MAKE)
        new_page_title = self.driver.find_element(*ClimateForecast.TITLE_HOW_TO_MAKE)
        assert new_page_title.is_displayed(), 'The title of the page does not match the expected value'
