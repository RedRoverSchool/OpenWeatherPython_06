from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


URL = 'https://openweathermap.org/'
BUTTON_PRICING = (By.XPATH, '//div[@id="desktop-menu"]//a[text()="Pricing"]')
DISPLAYED_TITLE = (By.CSS_SELECTOR, 'h1.breadcrumb-title')
FIELD_WEATHER_IN_YUOR_CITY = (By.CSS_SELECTOR, "#desktop-menu input[placeholder='Weather in your city']")
ALERT_NOTIFICATION = (By.CSS_SELECTOR, "#forecast_list_ul .alert.alert-warning")
STRING_ENTERED_CITY = (By.CSS_SELECTOR, "#search_str")


def test_TC_002_03_08_open_pricing(driver):
    driver.get(URL)
    button_pricing = driver.find_element(*BUTTON_PRICING)
    action_chains = ActionChains(driver)
    action_chains.move_to_element(button_pricing)
    driver.execute_script("arguments[0].click();", button_pricing)
    expected_title = "Pricing"
    displayed_title = driver.find_element(*DISPLAYED_TITLE).text
    assert displayed_title == expected_title

def test_TC_002_02_03_verify_result_of_search_for_invalid_city_name(driver, open_and_load_main_page, wait):
    search_weather_in_your_city = driver.find_element(*FIELD_WEATHER_IN_YUOR_CITY)
    entered_invalid_city_name = "LJKJJ"
    search_weather_in_your_city.send_keys(entered_invalid_city_name)
    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER).perform()
    displayed_notification = driver.find_element(*ALERT_NOTIFICATION)
    notification = displayed_notification.text
    assert notification == "×\nNot found"


