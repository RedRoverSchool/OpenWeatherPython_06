from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.by import By
URL = 'https://openweathermap.org/'
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url

def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url

def test_fill_search_city_field():
    driver.get('https://openweathermap.org/')
    search_city_field = driver.find_element(By.XPATH, "//div[@id='weather-widget']//input")
    search_city_field.send_keys('New York')

def test_fill_search_city_field2():
    driver.get('https://openweathermap.org/')
    search_city_field2 = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    search_city_field2.send_keys('London')
    time.sleep(10)



