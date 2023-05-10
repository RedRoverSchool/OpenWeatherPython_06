from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

logo_locator = (By.CSS_SELECTOR, ".logo > a > img")
allow_all_cookies_locator = (By.XPATH, '//*[contains(text(), "Allow all")]')

def test_TC_002_01_01_return_from_guide_page_to_main_page_by_clicking_on_logo(driver):
    driver.get('https://openweathermap.org/guide')
    driver.find_element(*logo_locator).click()
    assert driver.current_url == 'https://openweathermap.org/'

def test_TC_003_13_03_verify_visibility_and_clickability_of_allow_all_button(driver, open_and_load_main_page, wait):
    element = driver.find_element(*allow_all_cookies_locator)
    wait.until(EC.element_to_be_clickable(allow_all_cookies_locator))
    assert element.is_displayed() and element.is_enabled()