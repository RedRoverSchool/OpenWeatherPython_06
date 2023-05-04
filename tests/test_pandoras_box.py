from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = 'https://openweathermap.org/'
BUTTON_PRICING = (By.XPATH, '//div[@id="desktop-menu"]//a[text()="Pricing"]')
DISPLAYED_TITLE = (By.CSS_SELECTOR, 'h1.breadcrumb-title')

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


def test_TC_002_03_08_open_pricing(driver):
    driver.get(URL)
    button_pricing = driver.find_element(*BUTTON_PRICING)
    action_chains = ActionChains(driver)
    action_chains.move_to_element(button_pricing)
    driver.execute_script("arguments[0].click();", button_pricing)
    expected_title = "Pricing"
    displayed_title = driver.find_element(*DISPLAYED_TITLE).text
    assert displayed_title == expected_title


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