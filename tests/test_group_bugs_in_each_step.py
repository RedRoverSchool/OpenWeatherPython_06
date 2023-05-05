from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from conftest import URL
from selenium.webdriver.support.wait import WebDriverWait


def test_current_and_forecast_apis_functionality(driver):
    driver.get(URL)
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.XPATH, "//div[@class='owm-loader']")))
    cookies_button = driver.find_element(By.XPATH, "//button[text()='Allow all']")
    cookies_button.click()
    Current_and_Forecast_APIs = driver.find_element(By.XPATH, "//a[text()='Current and Forecast APIs']")
    Current_and_Forecast_APIs.click()
    assert 'https://openweathermap.org/api#current' in driver.current_url
