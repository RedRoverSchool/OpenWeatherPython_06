from pages.base_page import BasePage
from tests.test_group_lutz_squad.locators.page_with_map_locators import PageWithMapLocators


class PageWithMap(BasePage):

    def pressure_button_is_clickable(self, wait):
        pressure_button = self.driver.find_element(
            *PageWithMapLocators.PAGE_WITH_MAP_PRESSURE_BUTTON_LOCATOR)
        self.go_to_element(pressure_button)
        assert self.element_is_clickable(PageWithMapLocators.PAGE_WITH_MAP_PRESSURE_BUTTON_LOCATOR)
