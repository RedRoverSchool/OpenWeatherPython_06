from pages.base_page import BasePage
from tests.test_group_future_auto_qa.locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    locators = MainPageLocators()

    def get_header_search_field_attribute(self, attribute):
        search_placeholder = self.driver.find_element(*self.locators.HEADER_SEARCH_FIELD)
        return search_placeholder.get_attribute(attribute)

    def fill_city_search_field(self, city):
        input_city = self.driver.find_element(*self.locators.HEADER_SEARCH_FIELD)
        input_city.send_keys(city)

    def click_header_search_field(self):
        self.driver.find_element(*self.locators.HEADER_SEARCH_FIELD).click()

    def click_footer_product_collections_widgets(self, expected_link):
        self.allow_all_cookies()
        widgets_link = self.element_is_clickable(self.locators.FOOTER_WIDGETS)
        link_href = widgets_link.get_attribute('href')
        assert link_href == expected_link, "Incorrect link"
