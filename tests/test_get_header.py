import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def browser():
    driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_link(browser):
    browser.get("https://openweathermap.org/")
    time.sleep(5)
    assert 'openweathermap' in browser.current_url
    print(browser.current_url)


def test_check_title(browser):
    browser.get("https://openweathermap.org/cookies-settings")
    assert browser.title == 'Cookies settings - OpenWeatherMap'
