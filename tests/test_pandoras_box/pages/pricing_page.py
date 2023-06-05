from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PricingPage(BasePage):

    DISPLAYED_TITLE = (By.CSS_SELECTOR, 'h1.breadcrumb-title')
    pricing_url = 'https://openweathermap.org/price'
    button_detailed_pricing_locators = [(By.XPATH, '//*[@id="current"]//a[2]'),
                                        (By.XPATH, '//*[@id="history"]//a[2]')]

    def check_header_title(self, link_name):
        self.click_header_link(link_name)
        expected_title = "Pricing"
        displayed_title = self.driver.find_element(*self.DISPLAYED_TITLE).text
        assert displayed_title == expected_title


    def visibility_two_buttons_detailed_pricing(self):
        for pricing_locator in self.button_detailed_pricing_locators:
            button = self.driver.find_element(*pricing_locator)
            assert button.is_displayed()