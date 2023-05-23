import tests.tests_group_optimists_of_rationality_middle_devs.locators.main_page_locators
from tests.tests_group_optimists_of_rationality_middle_devs.locators.main_page_locators import *
import pytest


class TestTitle:
    def test_006_04_03_Verify_that_the_Subscribe_button_is_clickable_in_the_Pricing_and_limits_ection(self, driver, open_and_load_main_page):
        driver.find_element(*MainPageLocators.HEADER_DASHBOARD_LINK).click()
        for subscribe in MainPageLocators.PRICING_AND_LIMITS_MODULE:
            subscribe_button = driver.find_element(*subscribe)
            assert subscribe_button.is_enabled(), "Subscribe link is not clickable"

    def test_TC_006_03_01_verify_display_of_client_logos(self, driver, open_and_load_main_page):
        driver.find_element(*MainPageLocators.HEADER_DASHBOARD_LINK).click()
        assert driver.find_element(*MainPageLocators.DASHBOARD_LOGO_IMAGE).get_attribute(
            'src') != '', 'Dynamic image with customer logos not showing up in the "Our users" section'