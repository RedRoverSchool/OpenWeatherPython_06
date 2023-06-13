from pages.base_page import BasePage
from tests.group_files.the_hardworking_club.locators.locators_all import PricePageLocators

class PricePage(BasePage):

    URL_price_page = 'https://openweathermap.org/price'
    locators = PricePageLocators()

    def check_subscribe_button_redirect(self):
        self.driver.get(PricePage.URL_price_page)
        self.allow_all_cookies(timeout=2)
        self.driver.find_element(*self.locators.SUBSCRIBE_BUTTON).click()
        assert 'unauth_subscribe/onecall_30/base' in self.driver.current_url, "The billing-info page isn't open"

