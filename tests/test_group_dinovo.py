def test_should_open_given_link(driver):
    driver.get('https://openweathermap.org/')
    assert 'openweathermap' in driver.current_url


def test_check_page_title(driver):
    driver.get('https://openweathermap.org/')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


# from selenium import webdriver
# import pytest
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#
# # def test_open_page():
# def test_open_page(driver):
#     driver.get('https://openweathermap.org/')
#     driver.maximize_window()
#     assert 'openweathermap'in driver.current_url
#     print(driver.current_url)

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()

def test_open_page(driver):
    driver.get('https://openweathermap.org/')
    driver.maximize_window()
    assert 'openweathermap'in driver.current_url
    print(driver.current_url)


