from selenium.webdriver import ActionChains

from pages.base_page import BasePage
from tests.test_group_byte_me.locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    locators = MainPageLocators()

    def click_header_weather_in_your_city_field(self):
        weather_in_your_city_field = self.driver.find_element(*self.locators.WEATHER_IN_YOUR_CITY_FLD)
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(weather_in_your_city_field)
        self.driver.execute_script("arguments[0].click();", weather_in_your_city_field)
        return weather_in_your_city_field


    def fill_header_weather_in_your_city_field(self):
        input_weather_in_your_city_field = self.driver.find_element(*self.locators.WEATHER_IN_YOUR_CITY_FLD)
        input_weather_in_your_city_field.send_keys(*self.locators.REQUESTED_CITY)
        input_weather_in_your_city_field.submit()


    def displayed_text_is_the_same_as_the_entered_text(self, wait):
        displayed_text = wait.until(EC.visibility_of_element_located(self.locators.DISPLAYED_CITY)).text
        assert displayed_text == self.locators.REQUESTED_CITY
