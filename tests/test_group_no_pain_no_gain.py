from selenium.webdriver.common.by import By

URL = 'https://openweathermap.org/'

def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url

def test_check_page_title(driver):
    driver.get(URL)
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'

def test_check_logo_visibility(driver):
    driver.get(URL)
    logo = driver.find_element(By.CSS_SELECTOR, "#first-level-nav > li.logo > a > img")
    assert logo.is_displayed() == True
