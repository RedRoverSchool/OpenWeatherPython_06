import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://openweathermap.org/widgets-constructor'
api_key = (By.XPATH, "//input[@id='api-key']")
city_name = (By.CSS_SELECTOR, "#city-name")
type_widget_1 = (
By.XPATH, '//img[contains(@src, "themes/openweathermap/assets/vendor/owm/img/widgets/type-brown.png")]')
left_bottom_widget = (By.XPATH, '//div/*[@class="widget-left-menu widget-left-menu--brown"]')
widget_choose = (By.XPATH, "//li[@class = 'widget-choose__item']")
celsius_button = (By.CSS_SELECTOR, 'span#metric')
fahrenheit_button = (By.CSS_SELECTOR, 'span#imperial')

CURRENT_URL = "https://openweather.co.uk/privacy-policy"
XPATH_PRIVACY_POLICY_BUTTON = (By.XPATH, '//*[@id="footer-website"]/div/div[2]/div[2]/div/ul/li[2]/a')

# locators and URL for subscription page

URL_subscription_base = 'https://home.openweathermap.org/subscriptions/unauth_subscribe/onecall_30/base'

FIRST_NAME = (By.CSS_SELECTOR, '#invoice_form_first_name')
LAST_NAME = (By.CSS_SELECTOR, '#invoice_form_last_name')
ADDRESS_LINE_1 = (By.CSS_SELECTOR, '#invoice_form_address_line_1')
CITY = (By.CSS_SELECTOR, '#invoice_form_city')
POSTAL_CODE = (By.CSS_SELECTOR, '#invoice_form_postal_code')
PHONE = (By.CSS_SELECTOR, '#invoice_form_phone')
CONTINUE_TO_PAYMENT_BUTTON = (By.CSS_SELECTOR, "[name='commit']")


def test_TC_001_09_04_YourAPIKey_YourCityName_fields_visible(driver):
    driver.get(URL)
    your_api_key = driver.find_element(*api_key)
    your_city_name = driver.find_element(*city_name)
    assert your_api_key.is_displayed() and your_city_name.is_displayed()


@pytest.mark.skip(reason="Этот тест не проходит")
def test_TC_001_09_07_verify_display_of_bottom_widget_1_for_selected_type(driver):
    driver.get(URL)
    driver.find_element(*type_widget_1).click()
    left_bottom_widget_appeared = (WebDriverWait(driver, 10).until(EC.presence_of_element_located(left_bottom_widget)))
    assert left_bottom_widget_appeared.is_displayed()


def test_TC_001_09_02_Verify_that_3_widgets_are_displayed(driver, wait):
    driver.get(URL)
    widget_choose_item = driver.find_elements(*widget_choose)
    for widget in widget_choose_item:
        assert widget.is_displayed(), "Some widget is not displayed"



def test_TC_001_09_03_visibility_of_celsius(driver):
    driver.get(URL)
    celsius = driver.find_element(*celsius_button)
    assert celsius.is_displayed() and celsius.is_enabled()

def test_TC_003_12_06_verify_privacy_policy_is_opened_after_click(driver, open_and_load_main_page, wait):
    privacy_policy_button = wait.until(EC.element_to_be_clickable(XPATH_PRIVACY_POLICY_BUTTON))
    driver.execute_script("arguments[0].click();", privacy_policy_button)
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == CURRENT_URL

def test_TC_018_01_03_redirection_to_payment_service_page_for_logged_in_user(driver, open_and_load_main_page, wait, sign_in):
    driver.get(URL_subscription_base)
    first_name = driver.find_element(*FIRST_NAME)
    first_name.clear()
    first_name.send_keys('Testing')
    last_name = driver.find_element(*LAST_NAME)
    last_name.clear()
    last_name.send_keys('Uitesting')
    address_line_1 = driver.find_element(*ADDRESS_LINE_1)
    address_line_1.clear()
    address_line_1.send_keys('1100 Testing St')
    city = driver.find_element(*CITY)
    city.clear()
    city.send_keys('Test')
    postal_code = driver.find_element(*POSTAL_CODE)
    postal_code.clear()
    postal_code.send_keys('99500')
    phone = driver.find_element(*PHONE)
    phone.clear()
    phone.send_keys('+79071110099')
    driver.find_element(*CONTINUE_TO_PAYMENT_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.title_is('Openweather Ltd.'))
    assert 'checkout.stripe.com' in driver.current_url


