import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# main page selectors:
signin_button = (By.XPATH, "//li[@class='user-li']/*[text()='Sign in']")
def test_TC_002_03_19_signin_button_visible_clickable(driver):
    driver.get('https://openweathermap.org/')
    signin_button_displayed = driver.find_element(By.XPATH, "//li[@class='user-li']/*[text()='Sign in']")
    print(signin_button_displayed.is_displayed())
    time.sleep(5)
    print(signin_button_displayed.is_enabled())
    signin_button_displayed.click()
    driver.quit()