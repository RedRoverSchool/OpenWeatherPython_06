from pages.base_page import BasePage
from tests.test_group_lutz_squad.locators.partners_and_solutions_page_locators import PartnersAndSolutionsPageLocators as PAS


class PartnersAndSolutionsPage(BasePage):

    def more_details_link_is_clickable(self, wait):
        more_details_link = self.driver.find_element(*PAS.MORE_DETAILS_LOCATOR)
        self.go_to_element(more_details_link)
        self.element_is_displayed(PAS.MORE_DETAILS_LOCATOR, wait)
        assert self.element_is_clickable(PAS.MORE_DETAILS_LOCATOR)
