from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cities = ['New York', 'Los Angeles', 'Paris']


@pytest.mark.parametrize('city', cities)
def test_TC_001_04_01_visibility_of_8_lines_in_8_day_forecast_block(driver, open_and_load_main_page, city):
    search_city_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "input[placeholder='Search city']")))
    search_city_field.send_keys(city)
    search_button = driver.find_element(By.CSS_SELECTOR, "button[class ='button-round dark']")
    search_button.click()
    search_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'ul.search-dropdown-menu li:first-child span:first-child')))
    search_option.click()
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    c_temp = driver.find_element(By.CSS_SELECTOR, '.switch-container .option:nth-child(2)')
    c_temp.click()
    assert driver.find_element(By.XPATH,
                               "(//div[@class='day-list-values']/div/span[contains(text(), '°C')])[1]").is_displayed()
    assert driver.find_element(By.XPATH,
                               "(//div[@class='day-list-values']/div/span[contains(text(), '°C')])[2]").is_displayed()
    assert driver.find_element(By.XPATH,
                               "(//div[@class='day-list-values']/div/span[contains(text(), '°C')])[3]").is_displayed()
    assert driver.find_element(By.XPATH,
                               "(//div[@class='day-list-values']/div/span[contains(text(), '°C')])[4]").is_displayed()
    assert driver.find_element(By.XPATH,
                               "(//div[@class='day-list-values']/div/span[contains(text(), '°C')])[5]").is_displayed()
    assert driver.find_element(By.XPATH,
                               "(//div[@class='day-list-values']/div/span[contains(text(), '°C')])[6]").is_displayed()
    assert driver.find_element(By.XPATH,
                               "(//div[@class='day-list-values']/div/span[contains(text(), '°C')])[7]").is_displayed()
    assert driver.find_element(By.XPATH,
                               "(//div[@class='day-list-values']/div/span[contains(text(), '°C')])[8]").is_displayed()

