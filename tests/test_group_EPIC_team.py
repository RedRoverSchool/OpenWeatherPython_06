import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_TC_003_12_10_open_faq_page(driver, wait):
    driver.get('https://openweathermap.org/faq')
    assert driver.current_url == 'https://openweathermap.org/faq'
    driver.quit()