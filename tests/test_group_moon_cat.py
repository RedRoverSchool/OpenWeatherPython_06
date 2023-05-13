from selenium.webdriver.common.by import By


def test_TC_005_05_01_visibility_and_clickability_call_16_day_dailyforecast_data_link(driver, wait):
    driver.get('https://openweathermap.org/forecast16')
    element = driver.find_element(By.XPATH, "//a[@href='#16days']")
    assert element.is_displayed() and element.is_enabled()