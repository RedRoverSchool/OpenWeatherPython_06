from selenium.webdriver.support import expected_conditions as EC
from pages import base_page
from pages.base_page import BasePage
from tests.test_group_trust_me_i_am_engineer.locators.page_locators import SubscriptionsPageLocators

class SubscriptionsPage(BasePage):
    URL_SUBSCRIPTION = 'https://home.openweathermap.org/subscriptions/unauth_subscribe/onecall_30/base'
    locators = SubscriptionsPageLocators()

    def verify_redirect_to_payment_service_page_for_not_logged_in_user_in_organisation(self):
        self.driver.get(self.URL_SUBSCRIPTION)
        radiobutton = self.driver.find_element(*self.locators.RADIOBUTTON_ORGANISATIONS)
        radiobutton.click()
        email = self.driver.find_element(*self.locators.INPUT_EMAIL)
        email.send_keys('testemail@mail.com')







#     first_name = driver.find_element(*FIRST_NAME)
#     first_name.clear()
#     first_name.send_keys('Testing')
#     last_name = driver.find_element(*LAST_NAME)
#     last_name.clear()
#     last_name.send_keys('Uitesting')
#     address_line_1 = driver.find_element(*ADDRESS_LINE_1)
#     address_line_1.clear()
#     address_line_1.send_keys('1100 Testing St')
#     city = driver.find_element(*CITY)
#     city.clear()
#     city.send_keys('Test')
#     postal_code = driver.find_element(*POSTAL_CODE)
#     postal_code.clear()
#     postal_code.send_keys('99500')
#     phone = driver.find_element(*PHONE)
#     phone.clear()
#     phone.send_keys('+79071110099')
#     driver.find_element(*CONTINUE_TO_PAYMENT_BUTTON).click()
#     WebDriverWait(driver, 10).until(EC.title_is('Openweather Ltd.'))
#     assert 'checkout.stripe.com' in driver.current_url
