from selenium.webdriver.common.by import By


def test_TC_005_05_01_visibility_and_clickability_call_16_day_daily_forecast_data_link(driver, wait):
    driver.get('https://openweathermap.org/forecast16')
    element = driver.find_element(By.XPATH, "//a[@href='#16days']")
    assert element.is_displayed(), "Call 16 day/daily forecast data interactive icon is not visible on a page"
    assert element.is_enabled(), "Call 16 day/daily forecast data interactive icon is not clickable on a page"
    print(f'{element} is clickable')
