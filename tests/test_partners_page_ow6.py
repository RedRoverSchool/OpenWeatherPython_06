import pytest

from test_data import partners_page_data as PartnersData
from pages.partners_page import PartnersPage
from test_data.urls import PartnersPageUrls
from locators.locators import PartnersLocators


class TestPartnersPage:

    def test_tc_011_15_01_verify_correctly_redirected_the_link_apache_camel(self, driver, wait):
        page = PartnersPage(driver)
        apache_camel = PartnersPageUrls.APACHE_CAMEL_URL
        page.verify_redirected_the_link_apache_camel_to_a_new_window(apache_camel)

    def test_tc_011_15_02_verify_visibility_and_clickability_of_the_link_apache_camel(self, driver, wait):
        page = PartnersPage(driver)
        apache_camel = PartnersPageUrls.APACHE_CAMEL_URL
        page.verify_visibility_and_clickability_the_link_apache_camel_to_a_new_window(apache_camel)

    def test_tc_011_05_01_redirected_to_the_page_my_weather_indicator_in_launchpad_correctly(self, driver):
        page = PartnersPage(driver, PartnersPageUrls.PARTNERS_AND_SOLUTIONS)
        page.open_page()
        page.allow_all_cookies()
        page.find_element_and_click(PartnersLocators.UBUNTU_MY_WEATHER_INDICATOR)
        page.switch_to_new_window()
        page.check_for_redirection(PartnersPageUrls.WEATHER_INDICATOR_URL)

    def test_TC_011_13_01_verify_visibility_and_clickability_of_the_link_view_on_github_python(self, driver):
        partners_page = PartnersPage(driver)
        partners_page.verify_visibility_and_clickability_git_button_python()

    def test_TC_011_13_02_verify_correct_redirection_of_the_link_view_on_github_python(self, driver):
        partners_page = PartnersPage(driver)
        git_button_python = PartnersPageUrls.GIT_PYTHON_URL
        partners_page.verify_redirection_git_button_python_to_the_new_webpage(git_button_python)


    def test_tc_011_14_01_verify_visibility_and_clickability_of_the_github_button_php(self, driver, wait):
        page = PartnersPage(driver)
        page.verify_visibility_and_clickability_of_the_github_button_php(wait)

    def test_TC_011_03_01_verify_the_link_view_on_github_is_visible(self, driver):
        page = PartnersPage(driver)
        page.verify_the_link_view_on_github_is_visible()

    def test_TC_011_03_02_verify_the_link_view_on_github_is_clickable(self, driver):
        page = PartnersPage(driver)
        page.verify_the_link_view_on_github_is_clickable()

    def test_TC_011_03_01_verify_the_link_open_manual_is_visible(self, driver):
        page = PartnersPage(driver)
        page.verify_the_link_open_manual_is_visible()

    def test_TC_011_03_04_verify_the_link_open_manual_is_clickable(self, driver):
        page = PartnersPage(driver)
        page.verify_the_link_open_manual_is_clickable()


    def test_TC_011_01_03_verify_17_sections_are_visible(self, driver):
        page = PartnersPage(driver)
        page.verify_17_sections_are_visible()
    def test_TC_011_12_01_verify_the_link_in_raspberry_is_visible_and_clickable(self, driver):
        page = PartnersPage(driver, PartnersPageUrls.PARTNERS_AND_SOLUTIONS)
        page.open_page()
        page.link_visible_and_clickable(PartnersLocators.RASPBERRY)

    def test_TC_011_17_01_verify_the_mobile_link_leads_to_correct_page(self, driver):
        page = PartnersPage(driver, PartnersPageUrls.PARTNERS_AND_SOLUTIONS)
        page.open_page()
        page.scroll_to_the_element(PartnersLocators.MOBILE_APP_BLOCK)
        page.check_link(PartnersLocators.MOBILE_APP_LINK, PartnersPageUrls.MOBILE_APP)

    def test_TC_011_06_01_verify_the_first_link_in_android_section_is_visible_and_clickable(self, driver):
        page = PartnersPage(driver, PartnersPageUrls.PARTNERS_AND_SOLUTIONS)
        page.open_page()
        page.link_visible_and_clickable(PartnersLocators.ANDROID_FIRST_LINK)

    def test_TC_011_01_01_verify_that_Partners_and_solutions_page_title_is_correct(self, driver):
        page = PartnersPage(driver, PartnersPageUrls.PARTNERS_AND_SOLUTIONS)
        page.open_page()
        page.check_page_title(PartnersData.PARTNERS_PAGE_TITLE)

    def test_TC_011_01_02_verify_that_the_heading_of_the_page_equals_to_Partners_and_solutions(self, driver):
        page = PartnersPage(driver, PartnersPageUrls.PARTNERS_AND_SOLUTIONS)
        page.open_page()
        page.get_text_content_of_the_element(PartnersLocators.PARTNERS_PAGE_HEADING, PartnersData.PARTNERS_PAGE_HEADING)

    def test_TC_011_20_01_verify_that_the_info_board_message_at_the_top_of_the_page_is_displayed(self, driver):
        page = PartnersPage(driver, PartnersPageUrls.PARTNERS_AND_SOLUTIONS)
        page.open_page()
        page.get_text_content_of_the_element(PartnersLocators.PARTNERS_PAGE_INFO_BOARD, PartnersData.PARTNERS_PAGE_INFO_BOARD_TEXT)

    def test_TC_011_20_02_verify_the_color_of_the_info_board_message_at_the_top_of_the_page(self, driver):
        page = PartnersPage(driver, PartnersPageUrls.PARTNERS_AND_SOLUTIONS)
        page.open_page()
        page.get_background_color_of_the_element(PartnersLocators.PARTNERS_PAGE_INFO_BOARD, PartnersData.INFO_BOARD_BACKGROUND_COLOR)

    def test_TC_011_20_03_verify_that_the_Github_link_in_the_info_board_message_is_visible_and_clickable(self, driver):
        page = PartnersPage(driver, PartnersPageUrls.PARTNERS_AND_SOLUTIONS)
        page.open_page()
        page.link_visible_and_clickable(PartnersLocators.INFO_BOARD_GITHUB_LINK)

    def test_TC_011_20_04_Verify_that_the_Github_link_in_the_info_board_message_leads_to_correct_page(self, driver):
        page = PartnersPage(driver, PartnersPageUrls.PARTNERS_AND_SOLUTIONS)
        page.open_page()
        page.check_link_in_new_window(PartnersLocators.INFO_BOARD_GITHUB_LINK, PartnersPageUrls.INFO_BOARD_GITHUB)

    @pytest.mark.parametrize('anchor_locators', PartnersLocators.ANCHOR_LOCATORS)
    def test_TC_011_19_01_Verify_that_the_anchor_links_are_clickable(self, driver, anchor_locators):
        page = PartnersPage(driver, PartnersPageUrls.PARTNERS_AND_SOLUTIONS)
        page.open_page()
        page.element_is_clickable(anchor_locators)

    def test_TC_011_11_02_verify_redirection_awesome_button_to_the_right_website(self, driver):
        page = PartnersPage(driver, PartnersPageUrls.PARTNERS_AND_SOLUTIONS)
        page.verify_wordpress_awesome_weather_widget_leads_to_the_new_website()

    def test_TC_011_18_01_verify_redirection_view_solutions_button_to_the_right_website(self, driver):
        page = PartnersPage(driver, PartnersPageUrls.PARTNERS_AND_SOLUTIONS)
        page.verify_the_link_view_solutions_leads_to_the_new_website()
