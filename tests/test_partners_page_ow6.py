import pytest
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

    def test_tc_011_09_01_link_see_library_visibility(self, driver, wait):
        page = PartnersPage(driver, PartnersPageUrls.PARTNERS_AND_SOLUTIONS)
        page.open_page()
        page.link_see_library_visibility(wait)

    def test_tc_011_09_02_link_see_library_is_clickable(self, driver, wait):
        page = PartnersPage(driver, PartnersPageUrls.PARTNERS_AND_SOLUTIONS)
        page.open_page()
        page.link_see_library_is_clickable(wait)

    def test_tc_011_09_03_link_see_library_redirects_correctly(self, driver):
        page = PartnersPage(driver, PartnersPageUrls.PARTNERS_AND_SOLUTIONS)
        page.open_page()
        page.allow_all_cookies()
        page.find_element_and_click(PartnersLocators.LINK_SEE_LIBRARY)
        page.switch_to_new_window()
        page.check_for_redirection(PartnersPageUrls.GO_LIBRARY_PAGE)

