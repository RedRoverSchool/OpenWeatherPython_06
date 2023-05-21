from tests.test_group_snake_oil.links.all_links import DASHBOARD_PAGE_URL
from tests.test_group_snake_oil.pages.dashboard_page import DashboardPage
from tests.test_group_snake_oil.test_data.dashboard_page_data import EXPECTED_LINKS_AND_LOCATORS_SIGNED_IN, \
    EXPECTED_LINKS_AND_LOCATORS_SIGNED_OUT
import pytest


class TestDashboardPage:
    @pytest.mark.parametrize('locator, expected_url', EXPECTED_LINKS_AND_LOCATORS_SIGNED_OUT)
    def test_tc_006_02_04_verify_all_links_redirecting_to_the_respective_pages_signed_out(self, driver, locator,
                                                                                          expected_url):
        dashboard_page = DashboardPage(driver, DASHBOARD_PAGE_URL)
        dashboard_page.open_page()
        dashboard_page.allow_all_cookies()
        dashboard_page.verify_redirecting_to_expected_page(locator, expected_url)



