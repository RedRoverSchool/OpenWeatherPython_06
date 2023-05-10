from selenium.webdriver.common.by import By

URL = 'https://openweathermap.org/'
URL_WEATHER_API = 'https://openweathermap.org/api'
imperial_button_loc = (By.XPATH, '//*[@id="weather-widget"]/div[1]/div/div/div[1]/div[2]/div[3]')
current_temp_loc = (By.CSS_SELECTOR, "div.current-temp span.heading")
dashboard_button_loc = (By.XPATH, '//*[@id="desktop-menu"]/ul/li[3]/a')
dashboard_logo_image_loc = (By.XPATH, '/html/body/main/div[2]/div[8]/div/div/div[2]/img')
def test_TC_001_02_02_verify_temperature_switched_to_imperial_system(driver, open_and_load_main_page):
    driver.find_element(*imperial_button_loc).click()
    current_temp = driver.find_element(*current_temp_loc)
    assert "°F" in current_temp.text, "The current temperature is not in accordance with the imperial system"

def test_TC_006_03_01_verify_display_of_client_logos(driver, open_and_load_main_page):
    driver.find_element(*dashboard_button_loc).click()
    assert driver.find_element(*dashboard_logo_image_loc).get_attribute(
        'src') != '', 'Dynamic image with customer logos not showing up in the "Our users" section'