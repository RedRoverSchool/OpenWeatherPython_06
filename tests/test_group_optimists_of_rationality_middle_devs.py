from selenium.webdriver.common.by import By

URL = 'https://openweathermap.org/'
URL_WEATHER_API = 'https://openweathermap.org/api'
imperial_button_loc = (By.XPATH, '//*[@id="weather-widget"]/div[1]/div/div/div[1]/div[2]/div[3]')
current_temp_loc = (By.CSS_SELECTOR, "div.current-temp span.heading")

def test_TC_001_02_02_verify_temperature_switched_to_imperial_system(driver, open_and_load_main_page):
    driver.find_element(*imperial_button_loc).click()
    current_temp = driver.find_element(*current_temp_loc)
    assert "°F" in current_temp.text, "The current temperature is not in accordance with the imperial system"

 