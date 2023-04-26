from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
URL = 'https://openweathermap.org/'
displayed_current_location = (By.CSS_SELECTOR, '.icon-current-location')
logo = (By.XPATH, "//ul[@id='first-level-nav']/li/a/img")


def test_should_open_url(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url


def test_home_page_header(driver):
    driver.get(URL)
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    header = driver.find_element(By.CSS_SELECTOR, "h1")
    assert header.text == "OpenWeather", "Wrong h1 Header"
