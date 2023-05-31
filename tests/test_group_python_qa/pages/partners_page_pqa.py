from pages.base_page import BasePage
from tests.test_group_python_qa.locators.locators import PartnersPageLocators

class PartnersPage(BasePage):
    PARTNERS_AND_SOLUTION_PAGE_URL = "https://openweathermap.org/examples"
    BRIANDOWNS_GITHUB_URL = "http://briandowns.github.io/openweathermap/"
    locators = PartnersPageLocators()


    def link_See_library_visibility(self, wait):
        self.open_page()
        self.element_is_displayed(self.locators.LINK_SEE_LIBRARY, wait)
