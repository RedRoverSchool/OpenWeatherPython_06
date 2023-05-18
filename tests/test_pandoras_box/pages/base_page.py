from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.common.exceptions import TimeoutException


class BasePage:
    LINK_PRICING = (By.XPATH, '//div[@id="desktop-menu"]//a[text()="Pricing"]')
    FIELD_WEATHER_IN_YUOR_CITY = (By.CSS_SELECTOR, "#desktop-menu input[placeholder='Weather in your city']")

    def __init__(self, driver, link=None):
        self.driver = driver
        self.link = link

    def click_header_link(self, link_name):
        action_chains = ActionChains(self.driver)
        match link_name:
            case 'pricing':
                button_pricing = self.driver.find_element(*self.LINK_PRICING)
                action_chains.move_to_element(button_pricing)
                self.driver.execute_script("arguments[0].click();", button_pricing)

    def element_is_displayed(self, locator, wait):
        try:
            wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def enter_city_in_weather_in_your_city_field(self, city):
        input_city = self.driver.find_element(*self.FIELD_WEATHER_IN_YUOR_CITY)
        input_city.send_keys(city)

    def press_enter_button(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ENTER).perform()
