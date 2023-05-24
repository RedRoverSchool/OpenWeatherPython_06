
from selenium.webdriver.common.by import By

# main page selectors:
signin_button = (By.XPATH, "//li[@class='user-li']/*[text()='Sign in']")
def test_TC_002_03_19_signin_button_visible_clickable(driver, wait):
    driver.get('https://openweathermap.org/')
    sign_in_button = driver.find_element(*signin_button)
    assert sign_in_button.is_displayed()
    assert sign_in_button.is_enabled()