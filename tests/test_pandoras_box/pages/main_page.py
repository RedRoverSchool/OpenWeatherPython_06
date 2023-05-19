from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage

class MainPage(BasePage):
    LINK_PRICING = (By.XPATH, '//div[@id="desktop-menu"]//a[text()="Pricing"]')
    FIELD_WEATHER_IN_YUOR_CITY = (By.CSS_SELECTOR, "#desktop-menu input[placeholder='Weather in your city']")

    def enter_city_in_weather_in_your_city_field(self, city):
        input_city = self.driver.find_element(*self.FIELD_WEATHER_IN_YUOR_CITY)
        input_city.send_keys(city)