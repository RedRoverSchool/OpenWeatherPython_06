from test_data.main_page_data import data
import pytest

from oldTests.test_group_python_qa.locators.locators import MainPageLocators
from oldTests.test_group_python_qa.pages.main_page_pqa import MainPage
from oldTests.test_group_python_qa.links.links_all_pages import QUALITY_INFO_PAGE


class TestMainPage:

    @pytest.mark.parametrize('city', data["cityName"])
    def test_tc_001_04_01_visibility_of_8_lines_in_8_day_forecast_block(self, driver, open_and_load_main_page, wait,
                                                                        city):
        main_page = MainPage(driver)
        main_page.fill_city_search_field(city)
        main_page.click_search_button()
        main_page.choose_1st_option(wait)
        main_page.switch_to_c_temp()
        main_page.check_8_lines_are_displayed()

    def test_tc_021_01_01_visibility_of_agriculture_analytics_link(self, driver, open_and_load_main_page):
        main_page = MainPage(driver)
        main_page.visibility_of_agriculture_analytics_link()

    def test_TC_001_017_01_visibility_of_nwp_block(self, driver):
        quality_info_page = MainPage(driver, QUALITY_INFO_PAGE)
        quality_info_page.open_page()
        quality_info_page.visibility_of_nwp_block()

    def test_tc_003_05_01_subscription_module_title_displayed(self, driver, wait, open_and_load_main_page):
        main_page = MainPage(driver)
        main_page.element_is_displayed(MainPageLocators.SUBSCRIPTION_MODULE_BUTTON, wait)
