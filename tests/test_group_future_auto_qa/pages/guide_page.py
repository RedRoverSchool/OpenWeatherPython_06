from pages.base_page import BasePage
from tests.test_group_future_auto_qa.locators.guide_page_locators import GuidePageLocators


class GuidePage(BasePage):
    locators = GuidePageLocators()

    def open_guide_page(self):
        self.driver.get("https://openweathermap.org/guide")

    def check_weather_maps_collection_block_visibility(self):
        self.open_guide_page()
        weather_maps_collection = self.driver.find_element(*GuidePageLocators.WEATHER_MAPS_COLLECTION_BLOCK)
        assert weather_maps_collection.is_displayed(), "The Weather Maps collection is not displaying"
