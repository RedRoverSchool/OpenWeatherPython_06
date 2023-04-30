import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

URL = 'https://openweathermap.org/'


def test_open_page2(driver):
    driver.get('https://openweathermap.org/guide')
    time.sleep(5)
    assert 'guide' in driver.current_url
    print(driver.current_url)












