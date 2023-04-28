from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

URL = 'https://openweathermap.org/'
URL2 = 'https://openweathermap.org/guide/'
displayed_current_location = (By.CSS_SELECTOR, '.icon-current-location')
logo = (By.XPATH, "//ul[@id='first-level-nav']/li/a/img")


def test_should_open_url(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url


def test_home_page_header(driver):
    driver.get(URL)
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    header = driver.find_element(By.CSS_SELECTOR, "h1")
    assert header.text == "OpenWeather", "Wrong h1 Header"


def test_should_open_url2(driver):
    driver.get(URL2)
    assert 'openweathermap' in driver.current_url


def test_should_be_email_field_placeholder(driver):
    driver.get(URL)
    WebDriverWait(driver, 20).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    try:
        sign_in_top_menu = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//div[@id='desktop-menu']//li[@class='user-li']/a")))
        sign_in_top_menu.click()
    except TimeoutException as e:
        print(f"error occurred: {e}")
    try:
        expected_placeholder_text = "Enter email"
        email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user_email")))
        assert email_input.get_attribute("placeholder") == expected_placeholder_text, \
            "Email field placeholder text is incorrect"
    except TimeoutException as e:
        print(f"error occurred: {e}")
