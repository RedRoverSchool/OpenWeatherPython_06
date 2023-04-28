from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


def test_g(driver):
    driver.get('https://openweathermap.org/')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


def test_check_support_menu(driver):
    driver.get('https://openweathermap.org/')
    WebDriverWait(driver, 10).until_not(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    button_support = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#support-dropdown')))
    button_support.click()
    assert 'FAQ' and 'How to start' and 'Ask a question' in driver.page_source




