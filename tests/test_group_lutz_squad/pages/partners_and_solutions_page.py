from pages.base_page import BasePage
from tests.test_group_lutz_squad.locators.partners_and_solutions_page_locators import PartnersAndSolutionsPageLocators as PAS


class PartnersAndSolutionsPage(BasePage):

    def more_details_link_is_clickable(self, wait):
        more_details_link = self.driver.find_element(*PAS.MORE_DETAILS_LOCATOR)
        self.go_to_element(more_details_link)
        self.element_is_displayed(PAS.MORE_DETAILS_LOCATOR, wait)
        assert self.element_is_clickable(PAS.MORE_DETAILS_LOCATOR)

    def redirecting_to_more_details_with_source_code_page(self, wait):
        more_details_link = self.driver.find_element(*PAS.MORE_DETAILS_LOCATOR)
        self.driver.execute_script("arguments[0].click();", more_details_link)
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        weather_based = self.driver.find_element(*PAS.WEATHER_BASED_COMPAIGN_MANAGEMENT)
        assert weather_based.is_displayed(), 'Weather-based Campaign Management header is not on this page'

