from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://openweathermap.org/'
marketplace_link = (By.CSS_SELECTOR, '#desktop-menu ul li:nth-child(4) a')


def test_TC_002_03_07_verify_marketplace_link_redirects_to_valid_page(driver, open_and_load_main_page, wait):
    driver.set_window_size(1200, 800)
    driver.find_element(*marketplace_link).click()
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    assert driver.current_url == 'https://home.openweathermap.org/marketplace'