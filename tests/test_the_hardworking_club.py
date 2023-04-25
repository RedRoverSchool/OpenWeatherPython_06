import time
from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager  # CDM - it is class
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

URL = 'https://openweathermap.org/'


def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url


def test_check_page_title(driver):  # check title name
    driver.get('https://home.openweathermap.org/marketplace')
    assert driver.title == 'Marketplace: History Bulk, History Forecast Bulk, ' \
                           'Historical Weather Data by State for all ZIP codes, USA - OpenWeather'
