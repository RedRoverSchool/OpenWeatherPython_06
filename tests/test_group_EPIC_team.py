import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# main page selectors:
signin_button = (By.XPATH, "//li[@class='user-li']/*[text()='Sign in']")
def test_signin_button_visible_clickable(driver, wait):
    driver.get('https://openweathermap.org/')
    signin_button = driver.find_element(By.XPATH, "//li[@class='user-li']/*[text()='Sign in']")
    assert signin_button.is_displayed()
    assert signin_button.is_enabled()