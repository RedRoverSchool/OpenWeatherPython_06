from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

URL = 'https://openweathermap.org/'
cities = ['New York', 'Los Angeles', 'Paris']
load_div = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
search_dropdown = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li')
search_dropdown_option = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')
search_city_field = (By.CSS_SELECTOR, "input[placeholder='Search city']")
search_button = (By.CSS_SELECTOR, "button[class ='button-round dark']")
displayed_city = (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2')
sign_in_link = (By.CSS_SELECTOR, '.user-li a')
pricing_link = (By.CSS_SELECTOR, '#desktop-menu a[href="/price"]')
price_page_title = (By.CSS_SELECTOR, "h1[class='breadcrumb-title']")
accept_cookies = (By.CSS_SELECTOR, 'button.stick-footer-panel__link')
weather_in_your_city = (By.CSS_SELECTOR, "#desktop-menu input[placeholder='Weather in your city']")
search_in_header = (By.CSS_SELECTOR, "#desktop-menu form[role='search']")
city_query = (By.CSS_SELECTOR, '#search_str')


def test_TC_000_00_01_verify_sign_link_text_is_valid(driver, open_and_load_main_page, wait):
    driver.find_element(*accept_cookies).click()
    expected_text = 'Sign in'
    sign_in_text = driver.find_element(*sign_in_link).text
    assert sign_in_text == expected_text


def test_TC_000_00_02_verify_sign_in_link_is_clickable(driver, open_and_load_main_page, wait):
    element = driver.find_element(*sign_in_link)
    wait.until(EC.element_to_be_clickable(sign_in_link))
    assert element.is_displayed() and element.is_enabled()


def test_TC_000_00_03_verify_pricing_link_redirects_to_valid_page(driver, open_and_load_main_page, wait):
    driver.find_element(*pricing_link).click()
    pricing_text = driver.find_element(*price_page_title).text
    assert pricing_text == "Pricing"


def test_TC_000_00_04_verify_new_page_link_contains_valid_city_name(driver, open_and_load_main_page, wait):
    query = 'Florida'
    search_city = driver.find_element(*weather_in_your_city)
    search_city.send_keys(query)
    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER).perform()
    assert query in driver.current_url


def test_TC_000_00_05_verify_sign_in_link_redirects_to_valid_page(driver, open_and_load_main_page, wait):
    sign_link = wait.until(EC.presence_of_element_located(sign_in_link))
    driver.execute_script("arguments[0].click();", sign_link)
    assert "sign_in" in driver.current_url, f"\nWrong URL - {driver.current_url}"


@pytest.mark.parametrize('city', cities)
def test_TC_000_00_06_verify_result_of_city_searching_is_valid(driver, open_and_load_main_page, wait, city):
    search_city_input = driver.find_element(*search_city_field)
    search_city_input.send_keys(city)
    driver.find_element(*search_button).click()
    wait.until(EC.element_to_be_clickable(search_dropdown_option)).click()
    expected_city = city
    wait.until(EC.text_to_be_present_in_element(displayed_city, city))
    actual_city = driver.find_element(*displayed_city).text
    assert expected_city in actual_city


def test_TC_000_00_07_verify_search_button_is_clickable(driver, open_and_load_main_page, wait):
    search_city_input = driver.find_element(*search_city_field)
    search_city_input.send_keys('Paris')
    element = driver.find_element(*search_button)
    assert element.is_displayed() and element.is_enabled()
