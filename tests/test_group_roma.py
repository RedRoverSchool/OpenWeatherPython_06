from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://openweathermap.org/'


def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url


def test_button_search_exist(driver):
    driver.get(URL)
    btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    assert btn.text == "Search"

