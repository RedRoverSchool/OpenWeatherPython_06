import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://openweathermap.org/'


def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url


def test_check_page_title(driver):  # check title name
    driver.get('https://home.openweathermap.org/marketplace')
    assert driver.title == 'Marketplace: History Bulk, History Forecast Bulk, ' \
                           'Historical Weather Data by State for all ZIP codes, USA - OpenWeather'
