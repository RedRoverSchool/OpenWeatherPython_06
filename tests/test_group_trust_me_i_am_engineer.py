from datetime import datetime
from zoneinfo import ZoneInfo

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://openweathermap.org/'
URL_WEATHER_API = 'https://openweathermap.org/api'
metric_button_loc = (By.XPATH, "//div[@class='switch-container']/div[contains(text(), 'Metric')]")
imperial_button_loc = (By.XPATH, "//div[@class='switch-container']/div[contains(text(), 'Imperial')]")
current_temp_loc = (By.CSS_SELECTOR, "div.current-temp span.heading")
loc_date_time = (By.XPATH, "//div[@class='current-container mobile-padding']/div/span[@class='orange-text']")
our_initiatives_link = (By.CSS_SELECTOR, '#desktop-menu ul li:nth-child(7)')
learn_more_link = (By.CSS_SELECTOR, 'a[class="ow-btn round btn-black"]')
learn_more_page_title = (By.CSS_SELECTOR, "h1[class='breadcrumb-title']")
weather_api_page_title = (By.CSS_SELECTOR, "h1.breadcrumb-title")

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