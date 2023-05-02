from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


def test_displaying_requested_city_name_in_the_search_field(driver):
    driver.get('https://openweathermap.org/')
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    search_city_field.send_keys('Minsk')
    search_button = driver.find_element(By.CSS_SELECTOR, "button[class='button-round dark']")
    search_button.click()
    search_option = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')))
    search_option.click()
    expected_city = 'Minsk, BY'
    WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2'), 'Minsk, BY'))
    displayed_city = driver.find_element(By.CSS_SELECTOR, '.grid-container.grid-4-5 h2').text
    assert displayed_city == expected_city
