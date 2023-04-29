from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

URL = 'https://openweathermap.org/'
cities = ['New York', 'Los Angeles', 'Paris']
load_div = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
search_dropdown = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li')
search_dropdown_option = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')
search_city_field = (By.CSS_SELECTOR, "input[placeholder='Search city']")
search_button = (By.CSS_SELECTOR, "button[class ='button-round dark']")
displayed_city = (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2')
city = "Los Angeles, US"

def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url


def test_check_page_title(driver):
    driver.get(URL)
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


@pytest.mark.parametrize('city', cities)
def test_fill_search_city_field(driver, city):
    driver.get(URL)
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    search_city_input = driver.find_element(*search_city_field)
    search_city_input.send_keys(city)
    driver.find_element(*search_button).click()
    wait.until(EC.element_to_be_clickable(search_dropdown_option)).click()
    expected_city = city
    wait.until(EC.text_to_be_present_in_element(displayed_city, city))
    actual_city = driver.find_element(*displayed_city).text
    assert expected_city in actual_city


@pytest.mark.parametrize('city', cities)
def test_all_dropdown_options_should_contain_valid_city(driver, city):
    driver.get(URL)
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    search_city_input = driver.find_element(*search_city_field)
    search_city_input.send_keys(city)
    driver.find_element(*search_button).click()
    options = driver.find_elements(*search_dropdown)
    for option in options:
        assert city in option.text


def test_check_meteorological_conditions_are_displayed(driver):
    driver.get(URL)
    WebDriverWait(driver, 15).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    search_city_field_1 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "input[placeholder='Search city']")))
    search_city_field_1.send_keys(city)
    search_button_1 = driver.find_element(By.CSS_SELECTOR, "button[class ='button-round dark']")
    search_button_1.click()
    search_option = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:first-child span:first-child')))
    search_option.click()
    WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2'), city))
    displayed_city_1 = driver.find_element(By.CSS_SELECTOR, '.grid-container.grid-4-5 h2').text
    assert displayed_city_1 == city
    assert driver.find_element(By.CSS_SELECTOR, '.wind-line').is_displayed()
    assert driver.find_element(By.XPATH, '//span[text()="Humidity:"]').is_displayed()
    assert driver.find_element(By.XPATH, "//span[text()='Visibility:']").is_displayed()
    assert driver.find_element(By.CSS_SELECTOR, "li .icon-pressure").is_displayed()
    assert driver.find_element(By.XPATH, '//span[text()="Dew point:"] ').is_displayed()

def test_api_recommended_version(driver):
    driver.get(URL)
    WebDriverWait(driver, 15).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    button_api = WebDriverWait(driver, 35).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#desktop-menu>ul>li:nth-child(2)>a")))
    action_chains = ActionChains(driver)
    action_chains.move_to_element(button_api)
    driver.execute_script("arguments[0].click();", button_api)
    api_recommended_version = driver.find_element(By.XPATH, '//p/a[contains(text(), "One Call API 3.0")]').text
    assert api_recommended_version == "One Call API 3.0"

