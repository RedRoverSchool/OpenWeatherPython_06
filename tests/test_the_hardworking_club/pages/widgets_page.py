from tests.test_the_hardworking_club.pages.base_page import BasePage
from tests.test_the_hardworking_club.locators.locators_all import WidgetsPageLocators


class WidgetsPage(BasePage):
    locators = WidgetsPageLocators()


    def check_api_key_field(self):

        api_key_field = self.element_is_visible(self.locators.API_KEY)
        display = api_key_field.is_displayed()
        enable = api_key_field.is_enabled()
        return display, enable

    def check_city_name(self):
        city_name_field = self.element_is_visible(self.locators.CITY_NAME)
        display = city_name_field.is_displayed()
        enable = city_name_field.is_enabled()
        return display, enable





