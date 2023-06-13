from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://openweathermap.org/'
marketplace_link = (By.CSS_SELECTOR, '#desktop-menu ul li:nth-child(4) a')
logo = (By.CSS_SELECTOR, ".logo > a > img")
privacy_policy_link = (By.CSS_SELECTOR, 'div.section-content ul li:nth-child(2) a[href*="privacy-policy"]')


def test_TC_002_03_07_verify_marketplace_link_redirects_to_valid_page(driver, open_and_load_main_page, wait):
    driver.set_window_size(1200, 800)
    driver.find_element(*marketplace_link).click()
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    assert driver.current_url == 'https://home.openweathermap.org/marketplace'


def test_TC_002_01_07_verify_clicking_on_the_logo_from_page_Pricing_redirects_to_main_page(driver):
    driver.get('https://openweathermap.org/price')
    driver.find_element(*logo).click()
    assert driver.current_url == 'https://openweathermap.org/'


def test_TC_003_06_01_verify_privacy_policy_link_is_clickable(driver, open_and_load_main_page, wait):
    element = driver.find_element(*privacy_policy_link)
    wait.until(EC.element_to_be_clickable(privacy_policy_link))
    assert element.is_displayed() and element.is_enabled()
