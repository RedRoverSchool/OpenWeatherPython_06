from selenium.webdriver.common.by import By
import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://openweathermap.org/'

def test_open_page(driver):
    driver.get('https://openweathermap.org/')
    assert 'openweathermap' in driver.current_url
