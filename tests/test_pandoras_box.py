import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

URL = 'https://openweathermap.org/'
BUTTON_PRICING = (By.XPATH, '//div[@id="desktop-menu"]//a[text()="Pricing"]')
DISPLAYED_TITLE = (By.CSS_SELECTOR, 'h1.breadcrumb-title')

title_locator = (By.XPATH, '//p[text()="Product Collections"]')
URLs = ['https://openweathermap.org/',
        'https://openweathermap.org/guide'
        'https://openweathermap.org/api',
        'https://openweathermap.org/weather-dashboard',
        'https://openweathermap.org/price',
        'https://openweathermap.org/our-initiatives',
        'https://openweathermap.org/examples',
        'https://home.openweathermap.org/users/sign_in',
        'https://openweathermap.org/faq',
        'https://openweathermap.org/appid',
        'https://home.openweathermap.org/questions']

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
def test_TC_003_03_01_Product_Collections_title_is_visible(driver, URL):
    driver.get(URL)
    module_title = driver.find_element(*title_locator)
    assert module_title.is_displayed(), "Product Collections title is not visible"