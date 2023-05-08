from selenium.webdriver.common.by import By

COOKIES_BUTTON = (By.CLASS_NAME, "stick-footer-panel__link")
CURRENT_AND_FORECAST_APIS = (By.XPATH, "//a[text()='Current and Forecast APIs']")


def test_TC_003_12_04_current_and_forecast_apis_functionality(driver, open_and_load_main_page):
    driver.find_element(*COOKIES_BUTTON).click()
    driver.find_element(*CURRENT_AND_FORECAST_APIS).click()
    assert 'https://openweathermap.org/api#current' in driver.current_url
