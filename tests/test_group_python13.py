from selenium.webdriver.common.by import By
URL = 'https://openweathermap.org/'


def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url

def test_click_by_platform_leads_to_correct_page(driver):
    driver.get('https://openweather.co.uk/blog/')
    search_button = driver.find_element(By.LINK_TEXT, "PLATFORM")
    search_button.click()
    driver.implicitly_wait(10)
    assert driver.find_element(By.XPATH, "//*[contains(text(), 'The World Data League (WDL)')]")