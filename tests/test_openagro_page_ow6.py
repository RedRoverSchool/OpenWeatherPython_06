from test_data.all_links import OPENAGRO_PAGE, AGRICULTURAL_ANALYTICS_FORM
from pages.openagro_page import OpenAgroPage
from locators.locators import OpenAgroLocators


class TestOpenAgro:

    def test_tc_021_01_05_request_data_button_display_check(self, driver):
        openagro_page = OpenAgroPage(driver, OPENAGRO_PAGE)
        openagro_page.open_page()
        openagro_page.there_is_more_than_one_element_displayed_check(driver)

    def test_tc_021_01_06_redirection_to_agricultural_analytics_request_form(self, driver):
        openagro_page = OpenAgroPage(driver, OPENAGRO_PAGE)
        openagro_page.open_page()
        openagro_page.allow_all_cookies()
        openagro_page.find_element_and_click(OpenAgroLocators.REQUEST_DATA_BUTTON)
        openagro_page.switch_to_new_window()
        openagro_page.check_for_redirection(AGRICULTURAL_ANALYTICS_FORM)

