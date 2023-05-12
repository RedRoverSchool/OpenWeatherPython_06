import time

from selenium import webdriver
import pytest
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from keyboard import press


URL = 'https://openweathermap.org/'
LOAD_DIV = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
WEATHER_IN_YOUR_CITY_FLD = (By.CSS_SELECTOR, "#desktop-menu input:nth-child(1)")
REQUESTED_CITY = 'London, GB'
DISPLAYED_CITY = (By.CSS_SELECTOR, "table b a:nth-child(1)")


@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, 15)
    yield wait

def test_Search_City_Results_Are_Visible(driver, wait):
    driver.get(URL)
    wait.until_not(EC.presence_of_element_located(LOAD_DIV))
    weather_in_your_city_field = driver.find_element(*WEATHER_IN_YOUR_CITY_FLD)
    action_chains = ActionChains(driver)
    action_chains.move_to_element(weather_in_your_city_field)
    driver.execute_script("arguments[0].click();", weather_in_your_city_field)
    weather_in_your_city_field.send_keys(REQUESTED_CITY)
    weather_in_your_city_field.submit()
    displayed_city = driver.find_element(*DISPLAYED_CITY).text
    assert displayed_city == REQUESTED_CITY
