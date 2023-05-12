import os
import time
from datetime import datetime
from zoneinfo import ZoneInfo

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://openweathermap.org/'
URL_WEATHER_API = 'https://openweathermap.org/api'
URL_MARKETPLACE = 'https://home.openweathermap.org/marketplace'
URL_OUR_INITIATIVES = 'https://openweathermap.org/our-initiatives'
URL_WEATHER_CONDITIONS = 'https://openweathermap.org/weather-conditions'
metric_button_loc = (By.XPATH, "//div[@class='switch-container']/div[contains(text(), 'Metric')]")
imperial_button_loc = (By.XPATH, "//div[@class='switch-container']/div[contains(text(), 'Imperial')]")
current_temp_loc = (By.CSS_SELECTOR, "div.current-temp span.heading")
loc_date_time = (By.XPATH, "//div[@class='current-container mobile-padding']/div/span[@class='orange-text']")
our_initiatives_link = (By.CSS_SELECTOR, '#desktop-menu ul li:nth-child(7)')
learn_more_link = (By.CSS_SELECTOR, 'a[class="ow-btn round btn-black"]')
learn_more_page_title = (By.CSS_SELECTOR, "h1[class='breadcrumb-title']")
weather_api_page_title = (By.CSS_SELECTOR, "h1.breadcrumb-title")
history_bulk_title = (By.XPATH, "//h5/a[contains(text(), 'History Bulk')]")
history_bulk_search_location = (By.ID, "firstSearch")
history_bulk_search_import = (By.XPATH, "//button[contains(text(), 'Import')]")
button_import_csv = (By.XPATH, "//button[contains(text(), 'Import CSV file')]")
input_field_upload_file = (By.ID, "importCSV")
div_field_upload_file = (By.XPATH, "//*[@id='app']/div[2]/div")
location_name_table = (By.XPATH, "//table[@class='material-table']/tbody/tr/td[2]")
latitude_table = (By.XPATH, "//table[@class='material-table']/tbody/tr/td[3]")
longitude_table = (By.XPATH, "//table[@class='material-table']/tbody/tr/td[4]")
buttons_search_methods = (By.XPATH, "//div[@class='search-pop-up']/button")
search_pop_up = (By.CSS_SELECTOR, "div.search-pop-up")
first_search_items = (By.XPATH, "/html/body/div[4]/div[1]/span[2]/span")
search_pop_up_header = (By.XPATH, "//div[@class='pop-up-marker']/div[@class='pop-up-header']/h3")
headers_selector = (By.XPATH, "//h2[@style='margin-top: 0;']")
icon_list_description = (By.XPATH, "//table[@class='table table-bordered'][1]/tbody/tr/td[3]")
city_name = (By.CSS_SELECTOR, "div.current-container.mobile-padding div h2")
loc = (By.CSS_SELECTOR, "div.control-el svg.icon-current-location")
load_div = (By.CSS_SELECTOR, 'div.owm-loader-container > div')

def test_TC_001_02_01_verify_temperature_switched_on_metric_system(driver, open_and_load_main_page):
    driver.find_element(*metric_button_loc).click()
    current_temp = driver.find_element(*current_temp_loc)
    assert "°C" in current_temp.text, "The current temperature does not correspond to the metric system"

def test_TC_001_02_02_verify_temperature_switched_on_imperial_system(driver, open_and_load_main_page):
    driver.find_element(*imperial_button_loc).click()
    current_temp = driver.find_element(*current_temp_loc)
    assert "°F" in current_temp.text, "The current temperature does not correspond to the imperial system"

def test_TC_001_02_03_verify_temperature_metric_button_displayed_clickable(driver, open_and_load_main_page, wait):
    metric_button = wait.until(EC.element_to_be_clickable(metric_button_loc))
    assert metric_button.is_displayed() and metric_button.is_enabled(), \
        "The temperature switch button in the metric system is not displayed or is not clickable"

def test_TC_001_02_04_verify_temperature_imperial_button_displayed_clickable(driver, open_and_load_main_page, wait):
    imperial_button = wait.until(EC.element_to_be_clickable(imperial_button_loc))
    assert imperial_button.is_displayed() and imperial_button.is_enabled(), \
        "The temperature switch button in the imperial system is not displayed or is not clickable"

def test_TC_001_05_01_verify_the_current_date_and_time(driver, open_and_load_main_page):
    date_time = driver.find_element(*loc_date_time)
    date_time_str = f'{str(datetime.now(ZoneInfo("Europe/London")).year)} {date_time.text}'
    date_time_site = datetime.strptime(date_time_str, '%Y %b %d, %I:%M%p').replace(tzinfo=ZoneInfo('Europe/London'))
    date_time_now = datetime.now(ZoneInfo('Europe/London'))
    assert (date_time_now - date_time_site).total_seconds() <= 240, \
        "The current date and time does not match the date and time specified on the page"

def test_TC_010_01_03_verify_learn_more_link_redirects_to_valid_page(driver, open_and_load_main_page, wait):
    driver.find_element(*our_initiatives_link).click()
    driver.execute_script("window.scrollTo(0, 500)")
    driver.find_element(*learn_more_link).click()
    pricing_text = driver.find_element(*learn_more_page_title).text
    assert pricing_text == "Student initiative"

def test_TC_005_04_01_checking_title_page_weather_api(driver):
    expected_weather_api_page_title = "Weather API"
    driver.get(URL_WEATHER_API)
    page_title = driver.find_element(*weather_api_page_title)
    assert expected_weather_api_page_title == page_title.text, \
        "The title of the Weather API page does not match the expected title"

def test_TC_010_01_02_verify_learn_more_button_is_clickable(driver, open_and_load_main_page, wait):
    driver.find_element(*our_initiatives_link).click()
    wait.until(EC.element_to_be_clickable(our_initiatives_link))
    driver.execute_script("window.scrollTo(0, 500)")
    element = wait.until(EC.element_to_be_clickable(learn_more_link))
    assert element.is_displayed() and element.is_enabled()

def test_TC_007_02_01_verify_the_method_of_input_location(driver):
    expected_method_list = ['By location', 'By coordinates', 'Import']
    driver.get(URL_MARKETPLACE)
    driver.find_element(*history_bulk_title).click()
    driver.find_element(*history_bulk_search_location).click()
    methods = driver.find_elements(*buttons_search_methods)
    actual_method_list = [el.text for el in methods]
    assert expected_method_list == actual_method_list, \
        "The actual list of methods does not match the expected list of methods"

def test_TC_007_02_02_verify_search_by_location_name(driver, wait):
    expected_location = "Moscow"
    driver.get(URL_MARKETPLACE)
    driver.find_element(*history_bulk_title).click()
    search_loc = driver.find_element(*history_bulk_search_location)
    for ch in expected_location:
        search_loc.send_keys(ch)
        time.sleep(0.01)
    wait.until(EC.visibility_of_element_located(first_search_items))
    driver.find_element(*first_search_items).click()
    actual_search_result = wait.until(EC.visibility_of_element_located(search_pop_up_header))
    assert expected_location == actual_search_result.text

def test_TC_007_02_04_verify_search_by_import_csv(driver, wait):
    csv_file_path = os.path.abspath(os.getcwd() + "/../test_data/test_search_by_import.csv")
    f = open(csv_file_path, 'r')
    try:
        csv_str = f.readline()
    finally:
        f.close()
    expected_location, expected_latitude, expected_longitude = csv_str.split(";")

    driver.get(URL_MARKETPLACE)
    driver.find_element(*history_bulk_title).click()

    input_file = driver.find_element(*input_field_upload_file)
    div_input_file = driver.find_element(*div_field_upload_file)

    driver.execute_script("arguments[0].setAttribute('class','visible')", input_file)
    driver.execute_script("arguments[0].setAttribute('class','visible')", div_input_file)

    input_file.send_keys(csv_file_path)

    actual_location = driver.find_element(*location_name_table)
    actual_latitude = driver.find_element(*latitude_table)
    actual_longitude = driver.find_element(*longitude_table)
    assert actual_location.text.strip() == expected_location \
           and actual_latitude.text.strip() == expected_latitude \
           and actual_longitude.text.strip() == expected_longitude

def test_TC_010_01_02_verify_that_headers_are_visible_on_the_Our_initiatives_page(driver):
    datas = ['Education', 'Healthcare', 'Open Source', 'Weather stations']
    driver.get(URL_OUR_INITIATIVES)
    find_all_headers = driver.find_elements(*headers_selector)
    headers_on_page = [i.text for i in find_all_headers]
    assert datas == headers_on_page

def test_TC_001_10_04_weather_conditions_verify_list_of_description(driver):
    expected_list_description = ['clear sky', 'few clouds', 'scattered clouds', 'broken clouds', 'rain', 'snow']
    driver.get(URL_WEATHER_CONDITIONS)
    list_description = driver.find_elements(*icon_list_description)
    actual_list_description = [el.text for el in list_description]
    difference = set(expected_list_description) - set(actual_list_description)
    assert len(difference) == 0

def test_TC_001_05_02_verify_current_location(driver, open_and_load_main_page, wait):
    expected_city_name = "Chicago, US"
    driver.execute_cdp_cmd(
        "Browser.grantPermissions",
        {
            "origin": URL,
            "permissions": ["geolocation"]
        },
    )
    driver.execute_cdp_cmd(
        "Emulation.setGeolocationOverride",
        {
            "latitude": 41.8781,
            "longitude": -87.6298,
            "accuracy": 100,
        },
    )
    driver.find_element(*loc).click()
    wait.until_not(EC.presence_of_element_located(load_div))
    current_city_name = driver.find_element(*city_name)
    assert expected_city_name == current_city_name.text, \
        "The current name of the city does not match the expected name of the city"
