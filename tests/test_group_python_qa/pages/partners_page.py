from pages.base_page import BasePage
from tests.test_group_python_qa.locators.partners_page_locators import PartnersPageLocators

class PartnersPage(BasePage):
    PARTNERS_AND_SOLUTION_PAGE_URL = "https://openweathermap.org/examples"
    BRIANDOWNS_GITHUB_URL = "http://briandowns.github.io/openweathermap/"
    locators = PartnersPageLocators()


    def link_See_library_visibility(self):
        self.driver.get(self.PARTNERS_AND_SOLUTION_PAGE_URL)
        see_library_link = self.driver.find_element(*PartnersPageLocators.LINK_SEE_LIBRARY)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", see_library_link)
        assert see_library_link.is_displayed(), "The link is not displaying"

