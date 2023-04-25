from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

URL = 'https://openweathermap.org/'

def test_open_page(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url # проверка наличия строки в url

def test_open_page():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('https://openweathermap.org/')
    driver.maximize_window()
    temp_change = driver.find_element(By.XPATH, '//*[@id="weather-widget"]/div[1]/div/div/div[1]/div[2]')
    time.sleep(10)
    ActionChains(driver).drag_and_drop_by_offset(temp_change, 72, 0).perform()
    time.sleep(5)