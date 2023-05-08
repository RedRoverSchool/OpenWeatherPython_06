from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cities = ['New York', 'Los Angeles', 'Paris']
search_city_field_locator = "input[placeholder='Search city']"
search_button_locator = "button[class ='button-round dark']"
search_1st_option_locator = 'ul.search-dropdown-menu li:first-child span:first-child'
loading_screen_locator = 'div.owm-loader-container > div'
c_temp_locator = '.switch-container .option:nth-child(2)'
line_in_8_days_forecast_locator = "(//div[@class='day-list-values']/div/span[contains(text(), '°C')])"


@pytest.mark.parametrize('city', cities)
def test_TC_001_04_01_visibility_of_8_lines_in_8_day_forecast_block(driver, open_and_load_main_page, city):
    search_city_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, search_city_field_locator)))
    search_city_field.send_keys(city)
    search_button = driver.find_element(By.CSS_SELECTOR, search_button_locator)
    search_button.click()
    search_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, search_1st_option_locator)))
    search_option.click()
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, loading_screen_locator)))
    c_temp = driver.find_element(By.CSS_SELECTOR, c_temp_locator)
    c_temp.click()
    assert driver.find_element(By.XPATH, f"{line_in_8_days_forecast_locator}[1]").is_displayed()
    assert driver.find_element(By.XPATH, f"{line_in_8_days_forecast_locator}[2]").is_displayed()
    assert driver.find_element(By.XPATH, f"{line_in_8_days_forecast_locator}[3]").is_displayed()
    assert driver.find_element(By.XPATH, f"{line_in_8_days_forecast_locator}[4]").is_displayed()
    assert driver.find_element(By.XPATH, f"{line_in_8_days_forecast_locator}[5]").is_displayed()
    assert driver.find_element(By.XPATH, f"{line_in_8_days_forecast_locator}[6]").is_displayed()
    assert driver.find_element(By.XPATH, f"{line_in_8_days_forecast_locator}[7]").is_displayed()
    assert driver.find_element(By.XPATH, f"{line_in_8_days_forecast_locator}[8]").is_displayed()

