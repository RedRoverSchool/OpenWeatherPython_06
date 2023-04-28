import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = 'https://openweathermap.org/'
LOAD_COOKIE = (By.CSS_SELECTOR, 'div.owm-loader-container > div')

'''Support div bottoms'''
SUPPORT_BTN = (By.CSS_SELECTOR, '#desktop-menu li:nth-child(12)>div')
SUPPORT_FAQ = (By.CSS_SELECTOR, '#support-dropdown-menu li:nth-child(1)>a')
FAQ_TITLE = (By.XPATH, "//h1[contains(text(),'Frequently Asked Questions')]")
SUPPORT_HOW_TO_START = (By.CSS_SELECTOR, '#support-dropdown-menu li:nth-child(2)>a')
SUPPORT_ASK_A_QUESTION = (By.CSS_SELECTOR, '#support-dropdown-menu li:nth-child(3)>a')

@pytest.fixture()
def open_page(driver):
    driver.get(URL)
    driver.maximize_window()
    assert driver.current_url == URL, "Wrong page!"


@pytest.fixture()
def wait_upload(driver):
    try:
        wait = WebDriverWait(driver, 20)
        wait.until_not(EC.presence_of_element_located(LOAD_COOKIE))
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")
    yield wait

def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url


def test_check_page_title(driver):
    # function checks page title
    driver.get('https://openweathermap.org')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'

def test_verify_page_title(driver):
    driver.get('https://openweathermap.org')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'

def test_compare_page_title(driver):
    driver.get('https://openweathermap.org')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'

'''Testing Support menu'''
def test_desktop_menu_support(driver):
    try:
        driver.get(URL)
        wait_time = WebDriverWait(driver, 15)
        wait_time.until_not(EC.presence_of_element_located(LOAD_COOKIE))
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")

    try:
        desk_support = WebDriverWait(driver, 25).until(EC.element_to_be_clickable(SUPPORT_BTN))
        desk_support.click()
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")

def test_support_faq(driver, wait_upload, open_page):
    try:
        desk_support = WebDriverWait(driver, 25).until(EC.element_to_be_clickable(SUPPORT_BTN))
        desk_support.click()
        faq = WebDriverWait(driver, 25).until(EC.element_to_be_clickable(SUPPORT_FAQ))
        faq.click()
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")

    try:
        exp_title = 'Frequently Asked Questions'
        disp_title = WebDriverWait(driver, 25).until(EC.presence_of_element_located(FAQ_TITLE))
        disp_title_text = disp_title.text
        assert exp_title == disp_title_text
    except TimeoutException as e:
        print(f"TimeoutException occurred: {e}")
