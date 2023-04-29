import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

URL = 'https://openweathermap.org/'
cities = ['New York', 'Los Angeles', 'Paris']
load_div = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
search_dropdown = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li')
search_dropdown_option = (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:nth-child(1) span:nth-child(1)')
search_city_field = (By.CSS_SELECTOR, "input[placeholder='Search city']")
search_button = (By.CSS_SELECTOR, "button[class ='button-round dark']")
displayed_city = (By.CSS_SELECTOR, '.grid-container.grid-4-5 h2')


def test_open_page(driver):
    driver.get('https://openweathermap.org/')
    driver.maximize_window()
    assert 'openweathermap' in driver.current_url


def test_check_page_title(driver):
    driver.get('https://openweathermap.org/')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


@pytest.mark.parametrize('city', cities)
def test_fill_search_city_field(driver, city):
    driver.get('https://openweathermap.org/')
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


def test_search_field_present(driver):
    driver.get('https://openweathermap.org/')
    search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    assert search_city_field.is_displayed(), 'Search field not found on the Home page'


def test_search_field_placeholder(driver):
    driver.get('https://openweathermap.org/')
    search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
    expected_placeholder = 'Search city'
    actual_placeholder = search_city_field.get_attribute('placeholder')
    assert actual_placeholder == expected_placeholder, f'Search field placeholder is {actual_placeholder}, expected {expected_placeholder}'


def test_logo_is_presented(driver):
    driver.get('https://openweathermap.org/')
    logo = driver.find_element(By.XPATH, "//li[contains(@class, 'logo')]")
    assert logo.is_displayed(), "Logo not found on the Home page"


def test_check_facebook_link_in_footer(driver):
    driver.get('https://openweathermap.org/')
    footer_buttons = driver.find_elements(By.CSS_SELECTOR, '.social a')
    assert footer_buttons[0].get_attribute('href') == 'https://www.facebook.com/groups/270748973021342'


@pytest.mark.skip("need to refactor why this test sometimes doesn't work")
def test_captcha_sign_in_form(driver):
    driver.get(URL)
    search_sign_in = driver.find_element(By.CSS_SELECTOR, "#desktop-menu > ul > li.user-li > a")
    search_sign_in.click()
    search_create_account = driver.find_element(By.XPATH, "//a[text() = 'Create an Account.']")
    search_create_account.click()
    search_field_username = driver.find_element(By.CSS_SELECTOR, "#user_username")
    search_field_username.send_keys("Test123")
    search_field_email = driver.find_element(By.CSS_SELECTOR, "#user_email")
    search_field_email.send_keys("testbordiotatiana@gmail.com")
    search_field_password = driver.find_element(By.CSS_SELECTOR, "#user_password")
    search_field_password.send_keys("123test")
    search_field_repeatpas = driver.find_element(By.CSS_SELECTOR, "#user_password_confirmation")
    search_field_repeatpas.send_keys("123test")
    search_checkbox_age = driver.find_element(By.CSS_SELECTOR, "#agreement_is_age_confirmed")
    search_checkbox_age.click()
    search_checkbox_privacy = driver.find_element(By.CSS_SELECTOR, "#agreement_is_accepted")
    search_checkbox_privacy.click()
    search_btn_create_account = driver.find_element(By.CSS_SELECTOR, "#new_user > div:nth-child(21) > input")
    search_btn_create_account.click()
    search_failed_message = driver.find_element(By.CSS_SELECTOR, "#new_user > div:nth-child(20) > div.has-error > div")
    assert search_failed_message.is_displayed()
