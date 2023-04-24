from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_open_page(driver):
    driver.get('https://openweathermap.org/')
    driver.maximize_window()
    assert 'openweathermap' in driver.current_url