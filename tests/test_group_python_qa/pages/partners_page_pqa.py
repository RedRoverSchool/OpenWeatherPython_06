from pages.base_page import BasePage
from tests.test_group_python_qa.locators.locators import PartnersAndSolutionsPageLocators


class PartnersAndSolutionsPage(BasePage):
    locators = PartnersAndSolutionsPageLocators()

    def link_see_library_visibility(self, wait):
        self.open_page()
        self.element_is_displayed(self.locators.LINK_SEE_LIBRARY, wait)
