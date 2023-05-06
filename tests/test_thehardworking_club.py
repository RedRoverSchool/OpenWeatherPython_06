from selenium.webdriver.common.by import By


URL = 'https://openweathermap.org/widgets-constructor'
api_key = (By.XPATH, "//input[@id='api-key']")
city_name = (By.CSS_SELECTOR, "#city-name")

def test_TC_001_09_04_YourAPIKey_YourCityName_fields_visible(driver):
    driver.get(URL)
    your_api_key = driver.find_element(*api_key)
    your_city_name = driver.find_element(*city_name)
    assert your_api_key.is_displayed() and your_city_name.is_displayed()