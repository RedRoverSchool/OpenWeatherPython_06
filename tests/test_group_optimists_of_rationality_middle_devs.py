from selenium.webdriver.common.by import By

URL = 'https://openweathermap.org/'
URL_WEATHER_API = 'https://openweathermap.org/api'
imperial_button_loc = (By.XPATH, '//*[@id="weather-widget"]/div[1]/div/div/div[1]/div[2]/div[3]')
current_temp_loc = (By.CSS_SELECTOR, "div.current-temp span.heading")
dashboard_button_loc = (By.XPATH, '//*[@id="desktop-menu"]/ul/li[3]/a')
dashboard_logo_image_loc = (By.XPATH, '/html/body/main/div[2]/div[8]/div/div/div[2]/img')
pricing_and_limits_module_loc = [(By.XPATH, '//h2[text()="Pricing and limits"]'),
                                 (By.XPATH, '//html/body/main/div[2]/section/div/p'),
                                 (By.XPATH, '//html/body/main/div[2]/section/div/table')]
pricing_plans_subscribe_loc = [(By.XPATH, '//html/body/main/div[2]/section/div/table/tbody/tr[1]/th[3]/p/a'),
                               (By.XPATH, '//html/body/main/div[2]/section/div/table/tbody/tr[1]/th[4]/p/a'),
                               (By.XPATH, '//html/body/main/div[2]/section/div/table/tbody/tr[1]/th[5]/p/a'),
                               (By.XPATH, '//html/body/main/div[2]/section/div/table/tbody/tr[1]/th[6]/p/a')]


def test_TC_001_02_02_verify_temperature_switched_to_imperial_system(driver, open_and_load_main_page):
    driver.find_element(*imperial_button_loc).click()
    current_temp = driver.find_element(*current_temp_loc)
    assert "°F" in current_temp.text, "The current temperature is not in accordance with the imperial system"


def test_TC_006_03_01_verify_display_of_client_logos(driver, open_and_load_main_page):
    driver.find_element(*dashboard_button_loc).click()
    assert driver.find_element(*dashboard_logo_image_loc).get_attribute(
        'src') != '', 'Dynamic image with customer logos not showing up in the "Our users" section'


def test_TC_006_04_01_Verify_display_of_Pricing_and_limits_section(driver, open_and_load_main_page):
    driver.find_element(*dashboard_button_loc).click()
    for module in pricing_and_limits_module_loc:
        price_section = driver.find_element(*module)
        assert price_section.is_displayed(), 'No "pricing and limits" module'


def test_006_04_03_Verify_that_the_Subscribe_button_is_clickable_in_the_Pricing_and_limits_ection(driver,
                                                                                                  open_and_load_main_page):
    driver.find_element(*dashboard_button_loc).click()
    for subscribe in pricing_and_limits_module_loc:
        subscribe_button = driver.find_element(*subscribe)
        assert subscribe_button.is_enabled(), "Subscribe link is not clickable"
