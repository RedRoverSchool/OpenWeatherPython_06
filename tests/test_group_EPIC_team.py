import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_open_faq_page(driver):
    driver.get('https://openweathermap.org/faq')
    time.sleep(5)
    assert 'openweathermap' in driver.current_url
    print(driver.current_url)
    driver.quit()
