from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

selector_about = (By.CSS_SELECTOR, 'a[href*="about"]')
load_div = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
URL = ('https://openweathermap.org/')


def test_open_page(driver):
    driver.get('https://openweathermap.org/')
    driver.maximize_window()
    assert 'openweathermap' in driver.current_url


def test_check_about(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="stick-footer-panel"]/div')))
    driver.find_element(By.XPATH, '//*[@id="stick-footer-panel"]/div/div/div/div/div/button').click()
    driver.find_element(By.CSS_SELECTOR, 'a[href*="/about-us"]').click()
    title_about_us = driver.find_element(By.XPATH, '//div/h1/span["orange -text"]').text
    assert title_about_us == 'OpenWeather'
