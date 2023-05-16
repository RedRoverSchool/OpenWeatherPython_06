import time
from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def test_graphic_hourly_forecast():
    driver.get('https://openweathermap.org/')
    driver.maximize_window()
    search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    search_city_field.send_keys('Los Angeles')
    time.sleep(5)
    search_button = driver.find_element(By.CSS_SELECTOR, "button[class='button-round dark']")
    search_button.click()
    search_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')))
    time.sleep(5)
    search_option.click()
    time.sleep(5)
    expected_city = 'Los Angeles, US'
    displayed_city = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2')))
    displayed_city_text = displayed_city.text
    print(displayed_city_text)
    assert displayed_city_text == expected_city
    graphic_hourly_forecast = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'canvas[id=chart-component]')))
    assert graphic_hourly_forecast.is_displayed()
    print(graphic_hourly_forecast.is_displayed)