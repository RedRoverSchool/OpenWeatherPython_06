from selenium.webdriver.common.by import By

logo_locator = (By.CSS_SELECTOR, ".logo > a > img")


def test_TC_002_01_01_return_from_guide_page_to_main_page_by_clicking_on_logo(driver):
    driver.get('https://openweathermap.org/guide')
    driver.find_element(*logo_locator).click()
    assert driver.current_url == 'https://openweathermap.org/'
