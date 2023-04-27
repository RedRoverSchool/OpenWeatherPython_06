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
def test_check_page_title(driver):
    driver.get('https://openweathermap.org/')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'



