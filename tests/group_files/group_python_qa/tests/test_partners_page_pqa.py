from tests.group_files.group_python_qa.pages.partners_page_pqa import PartnersAndSolutions
from tests.group_files.group_python_qa.links.links_all_pages import PARTNERS_AND_SOLUTION_PAGE, GO_LIBRARY_PAGE
from tests.group_files.group_python_qa.locators.locators import PartnersAndSolutionsLocators as loc


class TestPartnersPage:

    def test_tc_011_05_01_redirected_to_the_page_my_weather_indicator_in_launchpad_correctly(self, driver):
        partners_page = PartnersAndSolutions(driver, PARTNERS_AND_SOLUTION_PAGE)
        partners_page.open_page()
        partners_page.allow_all_cookies()
        partners_page.find_element_and_click(loc.UBUNTU_MY_WEATHER_INDICATOR)
        partners_page.switch_to_new_window()
        partners_page.check_correct_redirection()

    def test_tc_011_09_01_link_see_library_visibility(self, driver, wait):
        partners_page = PartnersAndSolutions(driver, PARTNERS_AND_SOLUTION_PAGE)
        partners_page.open_page()
        partners_page.link_see_library_visibility(wait)

    def test_tc_011_09_02_link_see_library_is_clickable(self, driver, wait):
        partners_page = PartnersAndSolutions(driver, PARTNERS_AND_SOLUTION_PAGE)
        partners_page.open_page()
        partners_page.link_see_library_is_clickable(wait)

    def test_tc_011_09_03_link_see_library_redirects_correctly(self, driver):
        partners_page = PartnersAndSolutions(driver, PARTNERS_AND_SOLUTION_PAGE)
        partners_page.open_page()
        partners_page.allow_all_cookies()
        partners_page.find_element_and_click(loc.LINK_SEE_LIBRARY)
        partners_page.switch_to_new_window()
        partners_page.check_for_redirection(GO_LIBRARY_PAGE)



