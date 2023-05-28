from tests.test_group_future_auto_qa.locators.industries_page_locators import IndustriesPageLocators
from tests.test_group_future_auto_qa.pages.industries_page import IndustriesPage
import pytest


class TestIndustriesPage:

    talk_to_us_buttons_locators = IndustriesPageLocators.talk_to_us_buttons_locators

    @pytest.mark.parametrize("button_locator", talk_to_us_buttons_locators)
    def test_tc_012_03_03_checking_email_link_in_talk_to_us_buttons(self, driver, button_locator):
        page = IndustriesPage(driver)
        expected_link = "mailto:info@openweathermap.org"
        page.check_email_link_in_talk_to_us_button(button_locator, expected_link)

    request_a_trial_buttons_locators = IndustriesPageLocators.request_a_trial_buttons_locators
    all_buttons_locators = talk_to_us_buttons_locators + request_a_trial_buttons_locators

    @pytest.mark.parametrize("button_locator", all_buttons_locators)
    def test_tc_012_03_05_check_visibility_and_clickability_of_learn_more_and_talk_to_us_buttons(self, driver, wait, button_locator):
        page = IndustriesPage(driver)
        page.check_visibility_and_clickability_of_learn_more_and_talk_to_us_buttons(button_locator)

    def test_tc_012_03_06_verify_redirection_of_learn_more_button_in_agriculture_section(self, driver):
        page = IndustriesPage(driver)
        expected_link = "https://agromonitoring.com/"
        page.check_redirection_of_learn_more_button_in_agriculture_section(expected_link)


