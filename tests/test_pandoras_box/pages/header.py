from selenium.webdriver.common.by import By
from pages.base_page import BasePage
class Header(BasePage):

    logo_locator = (By.XPATH, '//*[@class="logo"]/a/img')
    search_field_locator = (By.XPATH, '//*[@placeholder="Weather in your city"]')

    def check_logo_is_visible(self):
        logo = self.driver.find_element(*self.logo_locator)
        assert logo.is_displayed(), "Logo is not visible"

    def enter_city_in_header_search_field(self, city):
        input_city = self.driver.find_element(*self.search_field_locator)
        input_city.send_keys(city)

    def check_open_maps(self, link_name):
        self.click_header_link(link_name)
        assert '/weathermap' in self.driver.current_url
