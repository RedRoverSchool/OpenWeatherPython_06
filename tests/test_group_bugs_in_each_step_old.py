from telnetlib import EC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

COOKIES_BUTTON = (By.CLASS_NAME, "stick-footer-panel__link")
CURRENT_AND_FORECAST_APIS = (By.XPATH, "//a[text()='Current and Forecast APIs']")


def test_TC_003_12_04_current_and_forecast_apis_functionality(driver, open_and_load_main_page):
    driver.find_element(*COOKIES_BUTTON).click()
    driver.find_element(*CURRENT_AND_FORECAST_APIS).click()
    assert 'https://openweathermap.org/api#current' in driver.current_url


def test_TC_003_03_02_verify_current_and_forecast_apis_is_clickable(driver, open_and_load_main_page, wait):
    element = driver.find_element(*CURRENT_AND_FORECAST_APIS)
    wait.until(EC.element_to_be_clickable(CURRENT_AND_FORECAST_APIS))
    assert element.is_displayed() and element.is_enabled()






