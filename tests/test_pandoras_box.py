from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import pytest

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

condition_URL = 'https://openweathermap.org/weather-conditions'
thunderstorm_locator = (By.XPATH, '//a[contains(@href, "#Thunderstorm")]/ancestor-or-self::table//tr')

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

def test_TC_001_12_01_thunderstorm_group_contains_items(driver):
    driver.get(condition_URL)
    codes_number = driver.find_elements(*thunderstorm_locator)
    assert len(codes_number) >= 3