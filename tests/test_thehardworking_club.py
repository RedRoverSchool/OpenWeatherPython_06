import os
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

URL = 'https://openweathermap.org/widgets-constructor'


def test_YourAPIKey_YourCityName_fields_visible(driver):
    driver.get(URL)
    driver.maximize_window()
    your_api_key = driver.find_element(By.XPATH, "//input[@id='api-key']")
    your_city_name = driver.find_element(By.CSS_SELECTOR, "#city-name")
    print(f'Your API Key field is displayed: {your_api_key.is_displayed()}')
    print(f'Your City Name field is displayed: {your_city_name.is_displayed()}')
