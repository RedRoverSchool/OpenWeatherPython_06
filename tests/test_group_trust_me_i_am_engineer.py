from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://openweathermap.org/'
load_div = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
metric_button_loc = (By.XPATH, "//div[@class='switch-container']/div[contains(text(), 'Metric')]")
imperial_button_loc = (By.XPATH, "//div[@class='switch-container']/div[contains(text(), 'Imperial')]")
current_temp_loc = (By.CSS_SELECTOR, "div.current-temp span.heading")

def test_TC_001_02_01_verify_temperature_switched_on_metric_system(driver, open_and_load_main_page, wait):
    driver.find_element(*metric_button_loc).click()
    wait.until_not(EC.presence_of_element_located(load_div))
    current_temp = driver.find_element(*current_temp_loc)
    assert "°C" in current_temp.text, "The current temperature does not correspond to the metric system"

def test_TC_001_02_02_verify_temperature_switched_on_imperial_system(driver, open_and_load_main_page, wait):
    driver.find_element(*imperial_button_loc).click()
    wait.until_not(EC.presence_of_element_located(load_div))
    current_temp = driver.find_element(*current_temp_loc)
    assert "°F" in current_temp.text, "The current temperature does not correspond to the imperial system"