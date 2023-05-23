from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from tests.test_the_hardworking_club.locators.locators_all import PricePageLocators

class PricePage(BasePage):

    URL_price_page = 'https://openweathermap.org/price'
    locators = PricePageLocators()

    def check_subscribe_button_redirect(self):
        self.driver.get(PricePage.URL_price_page)
        self.driver.find_element(*self.locators.COOKIE_BUTTON).click()
        self.driver.find_element(*self.locators.SUBSCRIBE_BUTTON).click()
        assert 'home.openweathermap.org/subscriptions' in self.driver.current_url \
               and 'onecall_30/base' in self.driver.current_url

