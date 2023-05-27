from pages.base_page import BasePage
from tests.test_group_python_qa.locators.locators import PartnersPageLocators


class PartnersPage(BasePage):
    locators = PartnersPageLocators()

    PARTNERS_AND_SOLUTION_PAGE_URL = "https://openweathermap.org/examples"
    BRIANDOWNS_GITHUB_URL = "http://briandowns.github.io/openweathermap/"

    def verify_link_See_library_visibility(self):
        self.driver.get(self.PARTNERS_AND_SOLUTION_PAGE_URL)
        see_library_link = self.driver.find_element(*self.locators.LINK_SEE_LIBRARY)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", see_library_link)
        assert see_library_link.is_displayed(), "The link is not displaying"
