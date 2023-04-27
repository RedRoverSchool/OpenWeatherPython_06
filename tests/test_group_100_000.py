import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = 'https://openweathermap.org/'
LOAD_COOKIE = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
SUPPORT_BTN = (By.CSS_SELECTOR, '#desktop-menu li:nth-child(12)>div')


def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url


def test_check_page_title(driver):
    # function checks page title
    driver.get('https://openweathermap.org')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'

def test_verify_page_title(driver):
    driver.get('https://openweathermap.org')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'

def test_compare_page_title(driver):
    driver.get('https://openweathermap.org')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'

def test_desktop_menu_support(driver):
    try:
        driver.get(URL)
        wait_time = WebDriverWait(driver, 15)
        wait_time.until_not(EC.presence_of_element_located(LOAD_COOKIE))
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")

    try:
        desk_support = WebDriverWait(driver, 25).until(EC.element_to_be_clickable(SUPPORT_BTN))
        desk_support.click()
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")
