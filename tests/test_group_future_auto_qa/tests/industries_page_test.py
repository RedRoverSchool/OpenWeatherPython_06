from tests.test_group_future_auto_qa.locators.industries_page_locators import IndustriesPageLocators
from tests.test_group_future_auto_qa.pages.industries_page import IndustriesPage
import pytest


class TestIndustriesPage:

    buttons_locators = IndustriesPageLocators.buttons_locators

    @pytest.mark.parametrize("button_locator", buttons_locators)
    def test_tc_012_03_03_checking_email_link_in_talk_to_us_buttons(self, driver, wait, button_locator):
        page = IndustriesPage(driver)
        expected_link = "mailto:info@openweathermap.org"
        page.check_email_link_in_talk_to_us_button(wait, button_locator, expected_link)
