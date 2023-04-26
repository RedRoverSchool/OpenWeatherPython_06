import time
from selenium.webdriver.common.by import By

URL = 'https://openweathermap.org/'
def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url

def test_website_description_visible(driver):
    driver.get(URL)
    time.sleep(10)
    expected_site_description_H2_text = driver.find_element(By.CSS_SELECTOR, ".black-text")
    expected_site_description_H2_text_is_visible = expected_site_description_H2_text.is_displayed()
    print('\n   #print = ', expected_site_description_H2_text, ' = ? is visible = ', expected_site_description_H2_text_is_visible)
    if expected_site_description_H2_text_is_visible:
        assert expected_site_description_H2_text_is_visible
