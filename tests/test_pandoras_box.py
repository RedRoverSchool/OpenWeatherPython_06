from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = 'https://openweathermap.org/'
BUTTON_PRICING = (By.XPATH, '//div[@id="desktop-menu"]//a[text()="Pricing"]')
DISPLAYED_TITLE = (By.CSS_SELECTOR, 'h1.breadcrumb-title')
FIELD_WEATHER_IN_YUOR_CITY = (By.CSS_SELECTOR, "#desktop-menu input[placeholder='Weather in your city']")
ALERT_NOTIFICATION = (By.CSS_SELECTOR, "#forecast_list_ul .alert.alert-warning")
STRING_ENTERED_CITY = (By.CSS_SELECTOR, "#search_str")


logo_locator = (By.XPATH, '//*[@class="logo"]/a/img')
URLs = ['https://openweathermap.org/',
        'https://openweathermap.org/guide',
        'https://openweathermap.org/api',
        'https://openweathermap.org/weather-dashboard',
        'https://openweathermap.org/price',
        'https://openweathermap.org/our-initiatives',
        'https://openweathermap.org/examples',
        'https://home.openweathermap.org/users/sign_in',
        'https://openweathermap.org/faq',
        'https://openweathermap.org/appid',
        'https://home.openweathermap.org/questions']

widget_constructor_URL = 'https://openweathermap.org/widgets-constructor'

metric_toggle = (By.XPATH, '//span[@id="metric"]')
imperial_units = (By.XPATH, '//span[text()="°F"]')
# widget_11 = (By.XPATH, '//*[@id="container-openweathermap-widget-11"]')
# widget_12 = (By.XPATH, '//*[@id="container-openweathermap-widget-12"]')
# widget_13 = (By.XPATH, '//*[@id="container-openweathermap-widget-13"]')
# widget_14 = (By.XPATH, '//*[@id="container-openweathermap-widget-14"]')
# widget_16 = (By.XPATH, '//*[@id="container-openweathermap-widget-15"]')
# widget_17 = (By.XPATH, '//*[@id="container-openweathermap-widget-16"]')
# widget_15 = (By.XPATH, '//*[@id="container-openweathermap-widget-17"]')
# widget_18 = (By.XPATH, '//*[@id="container-openweathermap-widget-18"]')
# widget_19 = (By.XPATH, '//*[@id="container-openweathermap-widget-19"]')

widgets_locators = [(By.XPATH, '//*[@id="container-openweathermap-widget-11"]'),
                    (By.XPATH, '//*[@id="container-openweathermap-widget-12"]'),
                    (By.XPATH, '//*[@id="container-openweathermap-widget-13"]'),
                    (By.XPATH, '//*[@id="container-openweathermap-widget-14"]'),
                    (By.XPATH, '//*[@id="container-openweathermap-widget-15"]'),
                    (By.XPATH, '//*[@id="container-openweathermap-widget-16"]'),
                    (By.XPATH, '//*[@id="container-openweathermap-widget-17"]'),
                    (By.XPATH, '//*[@id="container-openweathermap-widget-18"]'),
                    (By.XPATH, '//*[@id="container-openweathermap-widget-19"]')]


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
    wait.until(EC.presence_of_element_located(ALERT_NOTIFICATION))
    displayed_notification = driver.find_element(*ALERT_NOTIFICATION)
    notification = displayed_notification.text
    assert notification == "×\nNot found"


def test_TC_002_02_04_verify_displaying_entered_city_name_in_Search_field(driver, open_and_load_main_page, wait):
    search_weather_in_your_city = driver.find_element(*FIELD_WEATHER_IN_YUOR_CITY)
    entered_city_name = "LJKJJ"
    search_weather_in_your_city.send_keys(entered_city_name)
    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER).perform()
    wait.until(EC.presence_of_element_located(ALERT_NOTIFICATION) )
    search_result_city_name = driver.find_element(*STRING_ENTERED_CITY)
    found_city = search_result_city_name.get_property("value")
    assert found_city == entered_city_name

@pytest.mark.parametrize('URL', URLs)
def test_TC_002_01_03_Logo_is_visible(driver, wait, URL):
    driver.get(URL)
    logo = driver.find_element(*logo_locator)
    assert logo.is_displayed(), "Logo is not visible"


def test_TC_001_09_06_switched_on_Fahrenheit(driver):
    driver.get(widget_constructor_URL)
    toggle_position = driver.find_element(*metric_toggle)
    expected_position = 'color: rgb(235, 110, 75);'
    if toggle_position.get_attribute("style") == expected_position:
        toggle_position.click()
        for widget_locator in widgets_locators:
            WebDriverWait(driver, 15).until(EC.visibility_of_element_located(widget_locator))
        imperial_units_number = driver.find_elements(*imperial_units)
        assert len(imperial_units_number) == 14
    else:
        imperial_units_number = driver.find_elements(imperial_units)
        assert len(imperial_units_number) == 14