import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://openweathermap.org/"


def test_check_page_title(driver):
    # function checks page title
    driver.get('https://openweathermap.org')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url


def test_button_search_exist(driver):
    driver.get(URL)
    btn = driver.find_element(By.XPATH, "//button[@type='submit']")
    assert btn.text == "Search"


def test_open_page_map(driver):
    driver.get('https://openweathermap.org/weathermap?basemap=map&cities=true&layer=temperature&lat=30&lon=-20&zoom=5')
    driver.maximize_window()
    assert "weathermap" in driver.current_url