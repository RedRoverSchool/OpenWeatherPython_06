import time
from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://openweathermap.org/'
STUDENT_INITIATIVE_URL = 'https://openweathermap.org/our-initiatives/student-initiative'
search_city_field_locator = (By.CSS_SELECTOR, "input[placeholder='Search city']")
search_button_locator = (By.CSS_SELECTOR, "button[class ='button-round dark']")
search_dropdown_option = (By.CSS_SELECTOR, "ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)")
graphic_hourly_forecast_locator = (By.CSS_SELECTOR, "canvas[id=chart-component]")
weather_items_locator = (By.CSS_SELECTOR, "ul.weather-items")
weather_item_locator = (By.CSS_SELECTOR, 'ul.weather-items li:nth-child(1)')
website_link_locator = (By.CSS_SELECTOR, 'section#terms.anchor_el a[href="/"]')
ask_us_popup_locator = (By.CSS_SELECTOR, 'section#terms.anchor_el a[href="mailto:info@openweathermap.org"]')


def test_tc_001_08_01_graphic_hourly_forecast_is_displayed(driver, open_and_load_main_page, wait):
    driver.get(URL)
    graphic_hourly_forecast = driver.find_element(*graphic_hourly_forecast_locator)
    assert graphic_hourly_forecast.is_displayed()


def test_tc_001_08_02_weather_items_are_displayed(driver, open_and_load_main_page, wait):
    driver.get(URL)
    weather_items = driver.find_elements(*weather_item_locator)
    for weather_item in weather_items:
        assert weather_item.is_displayed()


def test_tc_010_02_06_verify_website_link_redirects_to_main_page(driver, open_and_load_main_page, wait):
    driver.get(STUDENT_INITIATIVE_URL)
    website_link = driver.find_element(*website_link_locator)
    driver.execute_script("arguments[0].click();", website_link)
    assert driver.current_url == URL


# ======= TC_006_01_01 =================================

button_dashboard_locator = (By.CSS_SELECTOR, '#desktop-menu a[href="/weather-dashboard"]')
dashboard_h1_locator = (By.CSS_SELECTOR, 'h1[class="h1-break"]')
dashboard_h3_locator = (By.CSS_SELECTOR, '.col-lg-6 h3')
dashboard_img_locator = (By.CSS_SELECTOR, '.col-md-6 img')


def test_tc_006_01_01_verify_description_of_open_weather_dashboard(driver, open_and_load_main_page, wait):
    driver.get(URL)
    driver.find_element(*button_dashboard_locator).click()
    driver.implicitly_wait(10)

    expected_dashboard_h1 = 'OpenWeather\nDashboard'
    actual_dashboard_h1 = driver.find_element(*dashboard_h1_locator)
    actual_dashboard_h1_text = actual_dashboard_h1.text
    assert actual_dashboard_h1_text == expected_dashboard_h1


def test_tc_006_01_01_dashboard_h3_displayed(driver, open_and_load_main_page, wait):
    driver.get(URL)
    driver.find_element(*button_dashboard_locator).click()
    driver.implicitly_wait(10)

    expected_dashboard_h3 = 'A visual tool for working with weather data and timely tracking of dangerous phenomena'
    actual_dashboard_h3 = driver.find_element(*dashboard_h3_locator)
    actual_dashboard_h3_text = actual_dashboard_h3.text
    assert actual_dashboard_h3_text == expected_dashboard_h3


def test_tc_006_01_01_dashboard_img_displayed(driver, open_and_load_main_page, wait):
    driver.get(URL)
    driver.find_element(*button_dashboard_locator).click()
    driver.implicitly_wait(10)

    expected_dashboard_img = driver.find_element(*dashboard_img_locator)
    assert expected_dashboard_img.is_displayed()


def test_tc_010_02_07_verify_correct_redirection_to_popup_window(driver, open_and_load_main_page, wait):
    driver.get(STUDENT_INITIATIVE_URL)
    ask_us_popup = driver.find_element(*ask_us_popup_locator)
    assert ask_us_popup.is_enabled() and ask_us_popup.is_displayed()
