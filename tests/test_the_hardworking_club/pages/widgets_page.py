from pages.base_page import BasePage
from tests.test_the_hardworking_club.locators.locators_all import WidgetsPageLocators
from conftest import driver


class WidgetsPage(BasePage):
    locators = WidgetsPageLocators()
    url_widgets_page = 'https://openweathermap.org/widgets-constructor'

    def check_input_fields(self):
        self.driver.get(WidgetsPage.url_widgets_page)
        fields = self.driver.find_elements(*self.locators.INPUT_FIELDS)
        for field in fields:
            assert field.is_displayed()

    def verify_display_of_bottom_widget_1_for_selected_type(self):
        self.driver.get(WidgetsPage.url_widgets_page)
        self.driver.find_element(*self.locators.TYPE_WIDGET_1).click()
        left_bottom_widget_appeared = self.element_is_visible(self.locators.LEFT_BOTTOM_WIDGET)
        assert left_bottom_widget_appeared.is_displayed()







