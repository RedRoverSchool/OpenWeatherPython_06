from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://openweathermap.org/'
def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url


def test_check_page_title(driver):
    # function checks page title
    driver.get('https://openweathermap.org')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'

def test_verify_page_title(driver):
    driver.get('https://openweathermap.org')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'

def test_compare_page_title(driver):
    driver.get('https://openweathermap.org')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'

def test_pricing_title(driver):
    driver.get('https://openweathermap.org/')
    WebDriverWait(driver, 10).until_not(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    button_pricing = WebDriverWait(driver, 35).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="first-level-nav"]//ul/li[5]/a')))
    button_pricing.click()
    pricing_text = driver.find_element(By.CSS_SELECTOR, ".breadcrumb-title").text
    assert pricing_text == "Pricing"