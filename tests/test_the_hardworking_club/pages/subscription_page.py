from pages.base_page import BasePage
from tests.test_the_hardworking_club.locators.locators_all import SubscriptionPagelocators
from selenium.webdriver.support.wait import WebDriverWait
import time

class SubscriptionPage(BasePage):
    URL_subscription_base = "https://home.openweathermap.org/subscriptions/unauth_subscribe/onecall_30/base"
    locators = SubscriptionPagelocators

    def verify_redirection_payment_service_page_for_not_logged_in_user(self):

        self.driver.get(SubscriptionPagelocators.URL_subscription_base)
        self.driver.find_element(*self.locators.RADIO_BUTTON_INDIVIDUAL).click()
        email = self.driver.find_element(*self.locators.TEXT_EDIT_EMAIL)
        email.click()
        email.send_keys('test@test.mail')
        first_name = self.driver.find_element(*self.locators.TEXT_EDIT_FIRST_NAME)
        first_name.clear()
        first_name.send_keys('Test')
        last_name = self.driver.find_element(*self.locators.TEXT_EDIT_LAST_NAME)
        last_name.clear()
        last_name.send_keys('Testing')
        address_line_1 = self.driver.find_element(*self.locators.TEXT_EDIT_ADDRESS_LINE_1)
        address_line_1.clear()
        address_line_1.send_keys('21 Vista')
        city = self.driver.find_element(*self.locators.TEXT_EDIT_CITY)
        city.clear()
        city.send_keys('San Mateo')
        postal_code = self.driver.find_element(*self.locators.TEXT_EDIT_POSTAL_CODE)
        postal_code.clear()
        postal_code.send_keys('94404')
        phone = self.driver.find_element(*self.locators.TEXT_EDIT_PHONE)
        phone.clear()
        phone.send_keys('(888)1234567')
        payment_button = self.driver.find_element(*self.locators.CONTINUE_TO_PAYMENT_BUTTON)
        payment_button.click()
        assert 'checkout.stripe.com' in self.driver.current_url






