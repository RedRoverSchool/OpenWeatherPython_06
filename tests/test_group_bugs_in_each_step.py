from webdriver_manager.core import driver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

URL = 'https://openweathermap.org/'



def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url



def test_check_page_title():
    test_should_open_given_link(driver)
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


def test_fill_search_city_field():
    driver.get('https://openweathermap.org/')
    search_city_field = driver.find_element(By.XPATH, "//div[@id='weather-widget']//input")
    search_city_field.send_keys('New York')
