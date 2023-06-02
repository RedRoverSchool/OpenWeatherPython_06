from tests.test_group_python_qa.pages.partners_page_pqa import PartnersAndSolutions
from tests.test_group_python_qa.links.links_all_pages import PARTNERS_AND_SOLUTION_PAGE
from tests.test_group_python_qa.locators.locators import PartnersAndSolutionsLocators as loc


class TestPartnersPage:

    def test_tc_011_05_01_redirected_to_the_page_my_weather_indicator_in_launchpad_correctly(self, driver):
        partners_page = PartnersAndSolutions(driver, PARTNERS_AND_SOLUTION_PAGE)
        partners_page.open_page()
        partners_page.allow_all_cookies()
        partners_page.find_element_and_click(loc.UBUNTU_MY_WEATHER_INDICATOR)
        partners_page.switch_to_new_window()
        partners_page.check_correct_redirection()

