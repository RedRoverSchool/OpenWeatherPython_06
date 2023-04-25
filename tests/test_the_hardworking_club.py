import time
from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager  # CDM - it is class
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


URL = 'https://openweathermap.org/'

def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url


def test_open_marketplace_page():
    driver.get('https://openweathermap.org/')    # open the main page
    time.sleep(5)
    # # search link and then click
    marketplace_link = driver.find_element(By.CSS_SELECTOR, "div#desktop-menu li:nth-child(4) a")
    marketplace_link.click()
    # # switch to new opened tab
    driver.switch_to.window(driver.window_handles[1])
    # # check if the current url is correct
    assert driver.current_url == 'https://home.openweathermap.org/marketplace'
    assert 'Marketplace' in driver.title
