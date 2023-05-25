from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from tests.test_the_hardworking_club.locators.locators_all import GuidePageLocators

class GuidePage(BasePage):

    url_guide_page = 'https://openweathermap.org/guide'
    locators = GuidePageLocators

    def check_the_all_links_are_visibility(self):

        self.driver.get(GuidePage.url_guide_page)
        link_text_list = [
            self.driver.find_element(*self.locators.SOLAR),
            self.driver.find_element(*self.locators.GLOBAL_WEATHER),
            self.driver.find_element(*self.locators.ROAD_RISK),
            self.driver.find_element(*self.locators.GLOBAL_PRECIP),
            self.driver.find_element(*self.locators.WEATHER_MAPS)
        ]
        for link_text in link_text_list:
            assert link_text.is_displayed()



