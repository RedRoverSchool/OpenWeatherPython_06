import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# main page selectors:
signin_button = (By.XPATH, "//li[@class='user-li']/*[text()='Sign in']")
Signin_URL = 'https://home.openweathermap.org/users/sign_in'

def test_TC_003_12_10_open_faq_page(driver, wait):
    driver.get('https://openweathermap.org/faq')
    assert driver.current_url == 'https://openweathermap.org/faq'

def test_TC_002_03_20_Sign_in_link_leads_to_correct_page(driver, open_and_load_main_page, wait):
    wait.until(EC.element_to_be_clickable(signin_button))
    driver.find_element(*signin_button).click()
    assert driver.current_url == Signin_URL
