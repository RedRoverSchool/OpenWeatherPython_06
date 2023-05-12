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
CURRENT_URL = "https://openweather.co.uk/privacy-policy"
XPATH_PRIVACY_POLICY_BUTTON = (By.XPATH, '//*[@id="footer-website"]/div/div[2]/div[2]/div/ul/li[2]/a')
subscribe_button = (By.XPATH, '//a[contains(text(), "Subscribe to One Call by Call")]')
cookie_button = (By.CSS_SELECTOR, 'button.stick-footer-panel__link')

def test_TC_001_09_04_YourAPIKey_YourCityName_fields_visible(driver):
    driver.get(URL)
    your_api_key = driver.find_element(*api_key)
    your_city_name = driver.find_element(*city_name)
    assert your_api_key.is_displayed() and your_city_name.is_displayed()


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


def test_TC_003_12_06_verify_privacy_policy_is_opened_after_click(driver, open_and_load_main_page, wait):
    privacy_policy_button = wait.until(EC.element_to_be_clickable(XPATH_PRIVACY_POLICY_BUTTON))
    driver.execute_script("arguments[0].click();", privacy_policy_button)
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == CURRENT_URL


def test_TC_008_01_01_subscribe_button_redirects(driver):
    driver.get('https://openweathermap.org/price')
    cookie_button_click = driver.find_element(*cookie_button)
    cookie_button_click.click()
    subscribe_button_click = driver.find_element(*subscribe_button)
    subscribe_button_click.click()
    assert 'home.openweathermap.org/subscriptions' in driver.current_url and 'onecall_30/base' in driver.current_url


