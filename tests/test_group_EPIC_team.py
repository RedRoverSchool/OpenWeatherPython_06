from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

URL = 'https://openweathermap.org/'
Locator_002_01_12_Logo = (By.CSS_SELECTOR, '#first-level-nav > li.logo > a > img')


def test_002_01_12_Verify_clicking_on_a_logo_from_the_Signin_page(driver):
    driver.get('https://home.openweathermap.org/users/sign_in')
    element = driver.find_element(*Locator_002_01_12_Logo)
    element.click()
    assert driver.current_url == 'https://openweathermap.org/'