from pages.base_page import BasePage
from tests.group_files.group_python_qa.locators.locators import SolarApiLocators


class SolarApi(BasePage):

    URL_SOLAR_API = "https://openweathermap.org/api/solar-energy-prediction"
    locator = SolarApiLocators()

    def check_for_correct_redirection_for_how_to_get_access_link(self, wait):
        self.open_page()
        self.find_element_and_click(self.locator.HOW_TO_GET_ACCESS_LINK_LOCATOR)
        self.find_element_and_click(self.locator.HOW_TO_GET_ACCESS_TITLE_LOCATOR)
        assert self.element_is_displayed(self.locator.HOW_TO_GET_ACCESS_TITLE_LOCATOR, wait)

    def visibility_of_product_concept_article_title(self, wait):
        self.open_page()
        self.element_is_displayed(self.locator.PRODUCT_CONCEPT_TITLE_LOCATOR, wait)


