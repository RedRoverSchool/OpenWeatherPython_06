import os
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://openweathermap.org/'
load_div = (By.CSS_SELECTOR, 'div.owm-loader-container > div')

@pytest.fixture(scope='function')
def driver():
    print('\nstart browser...')
    chrome_options = Options()
    if 'CI' in os.environ:
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        driver.set_window_size(1382, 754)
    else:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
    yield driver
    print('\nquit browser...')
    driver.quit()

@pytest.fixture()
def open_and_load_main_page(driver, wait):
    driver.get(URL)
    wait.until_not(EC.presence_of_element_located(load_div))


@pytest.fixture()
def wait(driver):
    wait = WebDriverWait(driver, 25)
    yield wait
