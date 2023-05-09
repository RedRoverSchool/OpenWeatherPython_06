from selenium.webdriver.common.by import By



URL = 'https://openweathermap.org/widgets-constructor'
URL_1 = 'https://openweathermap.org/weather-dashboard'


api_key = (By.XPATH, "//input[@id='api-key']")
city_name = (By.CSS_SELECTOR, "#city-name")
CONTACT_US = (By.CSS_SELECTOR, 'div.row p.below a.btn_like')
FITTER_PANEL = (By.CSS_SELECTOR, 'button.stick-footer-panel__link')


def test_TC_001_09_04_YourAPIKey_YourCityName_fields_visible(driver):
    driver.get(URL)
    your_api_key = driver.find_element(*api_key)
    your_city_name = driver.find_element(*city_name)
    assert your_api_key.is_displayed() and your_city_name.is_displayed()


def test_TC_006_05_03_button_Contact_Us_works(driver):

    driver.get(URL_1)
    my_CONTACT_US = driver.find_element(*CONTACT_US)
    my_FITTER_PANEL = driver.find_element(*FITTER_PANEL)
    my_FITTER_PANEL.click()
    my_CONTACT_US.click()
    assert my_CONTACT_US.is_enabled()