
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from tests.test_group_trust_me_i_am_engineer.locators.page_locators import SubscriptionsPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class SubscriptionsPage(BasePage):
    URL_SUBSCRIPTION = 'https://home.openweathermap.org/subscriptions/unauth_subscribe/onecall_30/base'
    locators = SubscriptionsPageLocators()

    def verify_error_messages_for_empty_required_fields_in_organisation(self):
        expected_error_message = "can't be blank"
        expected_number_of_error_message = 6
        self.driver.get(self.URL_SUBSCRIPTION)
        radiobutton = self.driver.find_element(*self.locators.RADIOBUTTON_ORGANISATIONS)
        radiobutton.click()
        button = self.driver.find_element(*self.locators.BUTTON_CONTINUE_TO_PAYMENT)
        button.click()
        error_message = self.elements_are_visible(self.locators.ERROR_MESSAGE)
        checks = 0
        for i in error_message:
            assert i.is_displayed()
            checks += 1
        assert checks == expected_number_of_error_message, \
            "An error message 'can't be blank' does not appeared for fields marked as required."


    def verify_redirect_to_payment_service_page_for_not_logged_in_user_in_organisation(self):
        self.driver.get(self.URL_SUBSCRIPTION)
        radiobutton = self.driver.find_element(*self.locators.RADIOBUTTON_ORGANISATIONS)
        radiobutton.click()
        email = self.driver.find_element(*self.locators.INPUT_EMAIL)
        email.send_keys('testemail@gmail.com')
        organisation = self.driver.find_element(*self.locators.INPUT_ORGANISATION)
        organisation.send_keys("TestName")
        address_line = self.driver.find_element(*self.locators.INPUT_ADDRESS_1)
        address_line.send_keys("1409 Dolores St")
        city = self.driver.find_element(*self.locators.INPUT_CITY)
        city.send_keys("San Francisco")
        postal_code = self.driver.find_element(*self.locators.INPUT_POSTCODE)
        postal_code.send_keys("94110")
        phone = self.driver.find_element(*self.locators.INPUT_PHONE_NUMBER)
        phone.send_keys("+19295678976")
        button = self.driver.find_element(*self.locators.BUTTON_CONTINUE_TO_PAYMENT)
        button.click()
        WebDriverWait(self.driver, timeout=20).until(EC.presence_of_element_located(self.locators.ELEMENT_STRIPE))
        assert 'checkout.stripe.com' in self.driver.current_url, \
            "'Continue to payment' button leads to incorrect page"
