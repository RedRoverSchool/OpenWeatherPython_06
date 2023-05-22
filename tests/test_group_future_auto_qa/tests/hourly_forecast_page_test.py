from tests.test_group_future_auto_qa.pages.hourly_forecast_page import HourlyForecastPage
from tests.test_group_future_auto_qa.locators.hourly_forecast_page_locators import HourlyForecastPageLocators
import pytest


class TestHourlyForecastPage:
    link_locators = HourlyForecastPageLocators.link_locators

    @pytest.mark.parametrize("link_locator", link_locators)
    def test_tc_005_07_01_redirects_of_anchor_links_in_a_block_on_right_side(self, driver, wait, link_locator):
        page = HourlyForecastPage(driver)
        page.check_redirects_of_anchor_links(wait, link_locator)
