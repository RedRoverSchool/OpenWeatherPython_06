from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


def test_check_page_title(driver):
    driver.get('https://openweathermap.org/')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


