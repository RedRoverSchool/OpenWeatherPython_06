from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pytest

URL = 'https://openweathermap.org/'
BUTTON_PRICING = (By.XPATH, '//div[@id="desktop-menu"]//a[text()="Pricing"]')
DISPLAYED_TITLE = (By.CSS_SELECTOR, 'h1.breadcrumb-title')
FIELD_WEATHER_IN_YUOR_CITY = (By.CSS_SELECTOR, "#desktop-menu input[placeholder='Weather in your city']")
ALERT_NOTIFICATION = (By.CSS_SELECTOR, "#forecast_list_ul .alert.alert-warning")
STRING_ENTERED_CITY = (By.CSS_SELECTOR, "#search_str")
BUTTON_GUIDE = (By.XPATH, "//div[@id='desktop-menu']//a[text()='Guide']")


logo_locator = (By.XPATH, '//*[@class="logo"]/a/img')
title_locator = (By.XPATH, '//p[text()="Product Collections"]')
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
maps_URL = 'https://openweathermap.org/weathermap'

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

result_locator = (By.XPATH, '//a[contains(@href, "city")]')
search_field_locator = (By.XPATH, '//*[@placeholder="Weather in your city"]')
condition_URL = 'https://openweathermap.org/weather-conditions'
thunderstorm_locator = (By.XPATH, '//a[contains(@href, "#Thunderstorm")]/ancestor-or-self::table//tr')

def test_TC_002_03_08_open_pricing(driver, open_and_load_main_page):
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

@pytest.mark.parametrize('URL', URLs)
def test_TC_003_03_01_Product_Collections_title_is_visible(driver, URL):
    driver.get(URL)
    module_title = driver.find_element(*title_locator)
    assert module_title.is_displayed(), "Product Collections title is not visible"

def test_TC_002_02_01_search_result_contains_city(driver, open_and_load_main_page, wait):
    search = driver.find_element(*search_field_locator)
    search.click()
    search.send_keys('Bangkok')
    search.send_keys(Keys.ENTER)
    driver.implicitly_wait(15)
    cities = driver.find_elements(*result_locator)
    for city in cities:
        assert 'Bangkok' in city.text

def test_TC_001_12_01_thunderstorm_group_contains_items(driver):
    driver.get(condition_URL)
    codes_number = driver.find_elements(*thunderstorm_locator)
    assert len(codes_number) >= 3


def test_TC_002_03_03_01_open_guide(driver, open_and_load_main_page):
    button_guide = driver.find_element(*BUTTON_GUIDE)
    action_chains = ActionChains(driver)
    action_chains.move_to_element(button_guide)
    driver.execute_script("arguments[0].click();", button_guide)
    expected_title = "Guide"
    displayed_title = driver.find_element(*DISPLAYED_TITLE).text
    assert displayed_title == expected_title



def test_TC_002_01_06_Verify_return_to_Main_page_from_Interactive_weather_maps(driver):
    driver.get(maps_URL)
    driver.find_element(*logo_locator).click()
    assert driver.current_url == 'https://openweathermap.org/'


