from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

search_city_field_locator = (By.CSS_SELECTOR, "input[placeholder='Search city']")
search_button_locator = (By.CSS_SELECTOR, "button[class='button-round dark']")
search_option_locator = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')
displayed_city_locator = (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2')


def testTC_001_01_02_01_displaying_requested_city_name_in_the_search_field(driver, open_and_load_main_page, wait):
    search_city_field = driver.find_element(*search_city_field_locator)
    search_city_field.send_keys('Minsk')
    search_button = driver.find_element(*search_button_locator)
    search_button.click()
    search_option = wait.until(
        EC.element_to_be_clickable((search_option_locator)))
    search_option.click()
    expected_city = 'Minsk, BY'
    wait.until(EC.text_to_be_present_in_element(
        (displayed_city_locator), expected_city))
    displayed_city = driver.find_element(*displayed_city_locator).text
    assert displayed_city == expected_city
