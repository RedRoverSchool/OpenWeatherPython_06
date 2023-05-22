from tests.test_group_future_auto_qa.pages.hourly_forecast_page import HourlyForecastPage
from tests.test_group_future_auto_qa.locators.hourly_forecast_page_locators import HourlyForecastPageLocators
import pytest


class TestHourlyForecastPage:
    link_locators = HourlyForecastPageLocators.link_locators

    @pytest.mark.parametrize("link_locator", link_locators)
    def test_tc_005_07_01_redirects_of_anchor_links_in_a_block_on_right_side(self, driver, wait, link_locator):
        page = HourlyForecastPage(driver)
        page.check_redirects_of_anchor_links(wait, link_locator)

    def test_tc_005_07_02_visibility_of_hourly_forecast_page_title(self, driver):
        page = HourlyForecastPage(driver)
        page_title = 'Hourly Weather Forecast 4 days - OpenWeatherMap'
        page.check_page_title(page_title)

    def test_tc_005_07_03_visibility_and_clickability_of_all_hourly_forecast_data_link(self, driver, wait):
        page = HourlyForecastPage(driver)
        page.check_clickability_and_visibility_of_call_hourly_forecast_data_link(wait)

