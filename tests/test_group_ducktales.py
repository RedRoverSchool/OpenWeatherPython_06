from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


URL_MAIN_PAGE = 'https://openweathermap.org/'

LOADER_CONTAINER = By.CSS_SELECTOR, 'div.owm-loader-container > div'
SEARCH_CITY_INPUT = By.CSS_SELECTOR, "input[placeholder='Search city']"
BTN_SEARCH = By.CSS_SELECTOR, "button[class ='button-round dark']"
SEARCH_DROPDOWN_MENU = By.CLASS_NAME, 'search-dropdown-menu'


def open_main_page(driver):
    driver.get(URL_MAIN_PAGE)
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        LOADER_CONTAINER))

def test_tc_001_01_01_verify_city_name_displayed_by_zip(driver):
    driver.get('https://openweathermap.org/')
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    search_city_field.send_keys('66002')
    search_button = driver.find_element(By.CSS_SELECTOR, "button[class ='button-round dark']")
    search_button.click()
    search_option = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')))
    search_option.click()
    expected_city = 'Atchison, US'
    WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2'), 'Atchison'))
    displayed_city = driver.find_element(By.CSS_SELECTOR, '.grid-container.grid-4-5 h2').text
    assert displayed_city == expected_city


def test_tc_001_01_02_verify_dropdown_options_contain_valid_value(driver):
    open_main_page(driver)
    driver.find_element(*SEARCH_CITY_INPUT).send_keys('California')
    driver.find_element(*BTN_SEARCH).click()
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(SEARCH_DROPDOWN_MENU))
    dropdown_list = driver.find_element(*SEARCH_DROPDOWN_MENU)
    for i in dropdown_list.find_elements(By.CSS_SELECTOR, 'li'):
        assert 'California' in i.text, 'Not all search suggestions in the drop-down list contain "California"'

