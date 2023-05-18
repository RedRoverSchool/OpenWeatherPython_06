from pages.base_page import BasePage
from tests.test_group_trust_me_i_am_engineer.locators.page_locators import MarketplacePageLocators

class MarketplacePage(BasePage):
    URL_MARKETPLACE = 'https://home.openweathermap.org/marketplace'
    locators = MarketplacePageLocators()

    def verify_the_method_of_input_location(self):
        expected_method_list = ['By location', 'By coordinates', 'Import']
        self.driver.get(self.URL_MARKETPLACE)
        self.driver.find_element(*self.locators.HISTORY_BILK_TITLE).click()
        self.driver.find_element(*self.locators.HISTORY_BILK_SEARCH_LOCATION).click()
        methods = self.driver.find_elements(*self.locators.BUTTON_SEARCH_METHODS)
        actual_method_list = [el.text for el in methods]
        assert expected_method_list == actual_method_list, \
            "The actual list of methods does not match the expected list of methods"