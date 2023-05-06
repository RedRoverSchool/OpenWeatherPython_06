from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.keys import Keys

URL = 'https://openweathermap.org/'
BUTTON_PRICING = (By.XPATH, '//div[@id="desktop-menu"]//a[text()="Pricing"]')
DISPLAYED_TITLE = (By.CSS_SELECTOR, 'h1.breadcrumb-title')

logo_locator = (By.XPATH, '//*[@class="logo"]/a/img')
URLs = ['https://openweathermap.org/',
        'https://openweathermap.org/guide',
        'https://openweathermap.org/api',
        'https://openweathermap.org/weather-dashboard',
        'https://openweathermap.org/price',
        'https://openweathermap.org/our-initiatives',
        'https://openweathermap.org/examples',
        'https://home.openweathermap.org/users/sign_in',
        'https://openweathermap.org/faq',
        'https://openweathermap.org/appid',
        'https://home.openweathermap.org/questions']

result_locator = (By.XPATH, '//a[contains(@href, "city")]')
search_field_locator = (By.XPATH, '//*[@placeholder="Weather in your city"]')

def test_TC_002_03_08_open_pricing(driver):
    driver.get(URL)
    button_pricing = driver.find_element(*BUTTON_PRICING)
    action_chains = ActionChains(driver)
    action_chains.move_to_element(button_pricing)
    driver.execute_script("arguments[0].click();", button_pricing)
    expected_title = "Pricing"
    displayed_title = driver.find_element(*DISPLAYED_TITLE).text
    assert displayed_title == expected_title

@pytest.mark.parametrize('URL', URLs)
def test_TC_002_01_03_Logo_is_visible(driver, wait, URL):
    driver.get(URL)
    logo = driver.find_element(*logo_locator)
    assert logo.is_displayed(), "Logo is not visible"

def test_TC_002_02_01_search_result_contains_city(driver, open_and_load_main_page, wait):
    search = driver.find_element(*search_field_locator)
    search.click()
    search.send_keys('Bangkok')
    search.send_keys(Keys.ENTER)
    driver.implicitly_wait(15)
    cities = driver.find_elements(*result_locator)
    for city in cities:
        assert 'Bangkok' in city.text