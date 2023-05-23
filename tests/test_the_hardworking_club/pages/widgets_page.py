from pages.base_page import BasePage
from tests.test_the_hardworking_club.locators.locators_all import WidgetsPageLocators
from conftest import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


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

    def check_the_specific_city_is_present(self):
        self.driver.get(WidgetsPage.url_widgets_page)
        search_field = self.driver.find_element(*self.locators.XPATH_CITY_NAME)
        search_field.clear()
        search_field.click()
        search_field.send_keys("Foster city")
        search_field_button = self.driver.find_element(*self.locators.XPATH_SEARCH_FIELD_BUTTON)
        search_field_button.click()
        wait = WebDriverWait(self.driver, 10)
        is_present = wait.until(EC.text_to_be_present_in_element(self.locators.XPATH_FIRST_BOTTOM_WIDGET_WINDOW, 'Foster City'))
        assert is_present


    def verify_that_3_widgets_are_displayed(self):
        self.driver.get(WidgetsPage.url_widgets_page)
        widget_choose_item = self.driver.find_elements(*self.locators.WIDGET_CHOOSE)
        for widget in widget_choose_item:
            assert widget.is_displayed(), "Some widget is not displayed"


    def verify_the_subtitle_of_the_page(self):
        self.driver.get(WidgetsPage.url_widgets_page)
        headline = self.driver.find_element(*self.locators.SUBTITLE_HEADLINE).text
        expected_title = "Get a code for posting a weather forecast widget on your site."
        assert headline == expected_title


    def verify_visibility_of_fahrenheit(self):
        self.driver.get(WidgetsPage.url_widgets_page)
        fahrenheit = self.driver.find_element(*self.locators.FAHRENHEIT_BUTTON)
        assert fahrenheit.is_displayed()







