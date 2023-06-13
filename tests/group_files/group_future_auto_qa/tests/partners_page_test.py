from tests.group_files.group_future_auto_qa.pages.partners_page import PartnersPage
from tests.group_files.group_future_auto_qa.test_data.urls import APACHE_CAMEL_URL


class TestPartnersPage:
    def test_TC_011_13_01_Verify_visibility_and_clickability_of_the_link_View_on_Github(self, driver):
        partners_page = PartnersPage(driver)
        partners_page.verify_visibility_and_clickability_git_button_python()

    def test_TC_011_13_02_Verify_correct_redirection_of_the_link_View_on_Github(self, driver):
        partners_page = PartnersPage(driver)
        partners_page.verify_redirection_git_button_python_to_the_new_webpage()

    def test_TC_011_13_03_visibility_and_clickability_of_the_link_View_on_Youtube(self, driver):
        partners_page = PartnersPage(driver)
        partners_page.verify_visibility_and_clickability_youtube_button_pyowm()

    def test_tc_011_15_01_verify_correctly_redirected_the_link_apache_camel(self, driver, wait):
        page = PartnersPage(driver)
        apache_camel = APACHE_CAMEL_URL
        page.verify_redirected_the_link_apache_camel_to_a_new_window(apache_camel)

    def test_tc_011_15_02_verify_visibility_and_clickability_of_the_link_apache_camel(self, driver, wait):
        page = PartnersPage(driver)
        apache_camel = APACHE_CAMEL_URL
        page.verify_visibility_and_clickability_the_link_apache_camel_to_a_new_window(apache_camel)

    def test_tc_011_14_01_verify_visibility_and_clickability_of_the_github_button_php(self, driver, wait):
        page = PartnersPage(driver)
        page.verify_visibility_and_clickability_of_the_github_button_php(wait)
