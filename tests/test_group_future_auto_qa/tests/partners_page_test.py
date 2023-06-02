from tests.test_group_future_auto_qa.pages.partners_page import PartnersPage
from tests.test_group_future_auto_qa.test_data.urls import APACHE_CAMEL_URL


def test_TC_011_13_01_Verify_visibility_and_clickability_of_the_link_View_on_Github(driver):
    partners_page = PartnersPage(driver)
    partners_page.verify_visibility_and_clickability_git_button_python()


def test_TC_011_13_02_Verify_correct_redirection_of_the_link_View_on_Github(driver):
    partners_page = PartnersPage(driver)
    partners_page.verify_redirection_git_button_python_to_the_new_webpage()


def test_tc_011_15_01_verify_correctly_redirected_the_link_apache_camel(driver, wait):
    page = PartnersPage(driver)
    apache_camel = APACHE_CAMEL_URL
    page.verify_redirected_the_link_apache_camel_to_a_new_window(apache_camel)
