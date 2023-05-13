from selenium.webdriver.common.by import By

URL_guide = 'https://openweathermap.org/guide'
how_to_start_link = (By.XPATH, "//a[contains(text(),'‘How to start and operate with API more efficientl')]")
call_16_day_daily_forecast_data = (By.XPATH, "//a[@href='#16days']")


def test_TC_005_05_01_visibility_and_clickability_call_16_day_dailyforecast_data_link(driver, wait):
    driver.get('https://openweathermap.org/forecast16')
    element = driver.find_element(*call_16_day_daily_forecast_data)
    assert element.is_displayed() and element.is_enabled()

def test_TC_004_04_01_verify_visibility_and_clickability_of_the_link(driver):
    driver.get(URL_guide)
    element = driver.find_element(*how_to_start_link)
    assert element.is_enabled() and element.is_displayed()
