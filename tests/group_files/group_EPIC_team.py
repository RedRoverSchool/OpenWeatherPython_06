import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def test_TC_003_12_10_open_faq_page(driver, wait):
    driver.get('https://openweathermap.org/faq')
    assert driver.current_url == 'https://openweathermap.org/faq'

signin_button = (By.XPATH, "//li[@class='user-li']/*[text()='Sign in']")

def test_TC_002_03_19_signin_button_visible_clickable(driver, wait):
    driver.get('https://openweathermap.org/')
    sign_in_button = driver.find_element(*signin_button)
    assert sign_in_button.is_displayed() and sign_in_button.is_enabled()
