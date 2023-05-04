from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

widget_constructor_URL = 'https://openweathermap.org/widgets-constructor'

metric_toggle = (By.XPATH, '//span[@id="metric"]')
imperial_units = (By.XPATH, '//span[text()="°F"]')
widget_11 = (By.XPATH, '//*[@id="container-openweathermap-widget-11"]')
widget_12 = (By.XPATH, '//*[@id="container-openweathermap-widget-12"]')
widget_13 = (By.XPATH, '//*[@id="container-openweathermap-widget-13"]')
widget_14 = (By.XPATH, '//*[@id="container-openweathermap-widget-14"]')
widget_16 = (By.XPATH, '//*[@id="container-openweathermap-widget-15"]')
widget_17 = (By.XPATH, '//*[@id="container-openweathermap-widget-16"]')
widget_15 = (By.XPATH, '//*[@id="container-openweathermap-widget-17"]')
widget_18 = (By.XPATH, '//*[@id="container-openweathermap-widget-18"]')
widget_19 = (By.XPATH, '//*[@id="container-openweathermap-widget-19"]')

def test_TC_001_09_06_switched_on_Fahrenheit(driver):
    driver.get(widget_constructor_URL)
    toggle_position = driver.find_element(*metric_toggle)
    expected_position = 'color: rgb(235, 110, 75);'
    if toggle_position.get_attribute("style") == expected_position:
        toggle_position.click()
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(widget_11))
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(widget_12))
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(widget_13))
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(widget_14))
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(widget_15))
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(widget_16))
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(widget_17))
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(widget_18))
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(widget_19))
        imperial_units_number = driver.find_elements(*imperial_units)
        assert len(imperial_units_number) == 14
    else:
        imperial_units_number = driver.find_elements(imperial_units)
        assert len(imperial_units_number) == 14