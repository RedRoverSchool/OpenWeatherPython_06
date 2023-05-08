from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

TO_IMPERIAL_BTN = By.XPATH, "//div[contains(text(),'Imperial: °F, mph')]"
TO_METRIC_BTN = By.XPATH, "//div[contains(text(),'Metric: °C, m/s')]"
LOADER_CONTAINER = By.CSS_SELECTOR, 'div.owm-loader-container > div'
SEARCH_CITY_INPUT = By.CSS_SELECTOR, "input[placeholder='Search city']"
BTN_SEARCH = By.CSS_SELECTOR, "button[class ='button-round dark']"
SEARCH_DROPDOWN_MENU = By.CLASS_NAME, 'search-dropdown-menu'
SEARCH_DROPDOWN_MENU_FIRST_CHILD = By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)'
SEARCH_DROPDOWN_MENU_FIRST_CHILD_TEXT = By.CSS_SELECTOR, '.grid-container.grid-4-5 h2'
MODULE_DOWNLOAD_OPENWEATHER_APP = By.XPATH, "//div[@class='my-5']/p"
FIRST_DAY_IN_8_DAY_FORECAST = By.CSS_SELECTOR, 'ul.day-list li:nth-child(1) span:nth-child(1)'

WEEKDAYS = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')


def test_tc_001_01_01_verify_city_name_displayed_by_zip(driver, open_and_load_main_page, wait):
    search_city_field = driver.find_element(*SEARCH_CITY_INPUT)
    search_city_field.send_keys('66002')
    search_button = driver.find_element(*BTN_SEARCH)
    search_button.click()
    search_option = wait.until(EC.element_to_be_clickable(SEARCH_DROPDOWN_MENU_FIRST_CHILD))
    search_option.click()
    expected_city = 'Atchison, US'
    wait.until(EC.text_to_be_present_in_element(SEARCH_DROPDOWN_MENU_FIRST_CHILD_TEXT, 'Atchison'))
    displayed_city = driver.find_element(* SEARCH_DROPDOWN_MENU_FIRST_CHILD_TEXT).text
    assert displayed_city == expected_city


def test_tc_001_01_02_verify_dropdown_options_contain_valid_value(driver, open_and_load_main_page, wait):
    driver.find_element(*SEARCH_CITY_INPUT).send_keys('California')
    driver.find_element(*BTN_SEARCH).click()
    wait.until(EC.element_to_be_clickable(SEARCH_DROPDOWN_MENU))
    dropdown_list = driver.find_element(*SEARCH_DROPDOWN_MENU)
    for i in dropdown_list.find_elements(By.CSS_SELECTOR, 'li'):
        assert 'California' in i.text, 'Not all search suggestions in the drop-down list contain "California"'


# TC_001.02.04_01 | Main page> Search city widget > Verify the buttons for metric and imperial are visible and clickable
def test_tc_001_02_04_01_switch_toggle_buttons(driver, open_and_load_main_page, wait):
    # switch the temperature system to imperial
    imperial_button = driver.find_element(*TO_IMPERIAL_BTN)
    imperial_button.click()
    metric_button = driver.find_element(*TO_METRIC_BTN)
    metric_button.click()
    # Verify that toggle buttons are displayed and clickable
    assert metric_button.is_displayed() and imperial_button.is_displayed()
    assert metric_button.is_enabled() and imperial_button.is_enabled()


def test_tc_003_09_01_the_module_title_display(driver, open_and_load_main_page, wait):
    expected_module_title = "Download OpenWeather app"
    module_download_openweather_app = driver.find_element(*MODULE_DOWNLOAD_OPENWEATHER_APP)
    module_download_openweather_app.location_once_scrolled_into_view
    actual_module_title = module_download_openweather_app.text
    assert actual_module_title == expected_module_title


def test_TC_001_04_03_verify_in_day_list_first_element_day_by_week(driver, open_and_load_main_page):
    day_by_weak = driver.find_element(*FIRST_DAY_IN_8_DAY_FORECAST).text[:3]
    day_by_computer = datetime.now().weekday()
    today = WEEKDAYS[day_by_computer]
    assert day_by_weak == f'{today}'


def test_tc_001_04_05_main_page_search_city_widget_8_day_forecast_first_element_number_day(driver, open_and_load_main_page):
    number_day = driver.find_element(*FIRST_DAY_IN_8_DAY_FORECAST).text[-2:]
    if number_day.startswith('0'):
        number_day = number_day[1:]
    number_day_by_computer = datetime.now().day
    assert number_day == f'{number_day_by_computer}'

