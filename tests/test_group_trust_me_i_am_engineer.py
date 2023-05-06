from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://openweathermap.org/'
load_div = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
metric_button_loc = (By.XPATH, "//div[@class='switch-container']/div[contains(text(), 'Metric')]")
imperial_button_loc = (By.XPATH, "//div[@class='switch-container']/div[contains(text(), 'Imperial')]")
current_temp_loc = (By.CSS_SELECTOR, "div.current-temp span.heading")

def test_TC_001_02_01_verify_temperature_switched_on_metric_system(driver, open_and_load_main_page):
    driver.find_element(*metric_button_loc).click()
    current_temp = driver.find_element(*current_temp_loc)
    assert "°C" in current_temp.text, "The current temperature does not correspond to the metric system"

def test_TC_001_02_02_verify_temperature_switched_on_imperial_system(driver, open_and_load_main_page):
    driver.find_element(*imperial_button_loc).click()
    current_temp = driver.find_element(*current_temp_loc)
    assert "°F" in current_temp.text, "The current temperature does not correspond to the imperial system"

def test_TC_001_02_03_verify_temperature_metric_button_displayed_clickable(driver, open_and_load_main_page, wait):
    metric_button = wait.until(EC.element_to_be_clickable(metric_button_loc))
    assert metric_button.is_displayed() and metric_button.is_enabled(), \
        "The temperature switch button in the metric system is not displayed or is not clickable"

def test_TC_001_02_04_verify_temperature_imperial_button_displayed_clickable(driver, open_and_load_main_page, wait):
    imperial_button = wait.until(EC.element_to_be_clickable(imperial_button_loc))
    assert imperial_button.is_displayed() and imperial_button.is_enabled(), \
        "The temperature switch button in the imperial system is not displayed or is not clickable"