import time
from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://openweathermap.org/'
search_city_field_locator = (By.CSS_SELECTOR, "input[placeholder='Search city']")
search_button_locator = (By.CSS_SELECTOR, "button[class ='button-round dark']")
search_dropdown_option = (By.CSS_SELECTOR, "ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)")
graphic_hourly_forecast_locator = (By.CSS_SELECTOR, "canvas[id=chart-component]")
weather_items_locator = (By.CSS_SELECTOR, "ul.weather-items")
weather_item_locator = (By.CSS_SELECTOR, 'ul.weather-items li:nth-child(1)')

def test_tc_001_08_01_graphic_hourly_forecast_is_displayed(driver, open_and_load_main_page, wait):
    driver.get(URL)
    graphic_hourly_forecast = driver.find_element(*graphic_hourly_forecast_locator)
    assert graphic_hourly_forecast.is_displayed()


def test_tc_001_08_02_weather_items_are_displayed(driver, open_and_load_main_page, wait):
    driver.get(URL)
    weather_items = driver.find_elements(*weather_item_locator)
    for weather_item in weather_items:
        assert weather_item.is_displayed()



