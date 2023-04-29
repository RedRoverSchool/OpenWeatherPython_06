from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.action_chains import ActionChains

URL = 'https://openweathermap.org/'


def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url


def test_check_page_title(driver):
    driver.get(URL)
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


def test_section_where_to(driver):
    driver.get(URL)
    element_section_where_to_h1 = driver.find_element(By.CSS_SELECTOR, ".mobile-padding h1 .white-text")
    assert element_section_where_to_h1.text == 'OpenWeather'

    element_section_where_to_h2 = driver.find_element(By.CSS_SELECTOR, ".mobile-padding h2 .black-text")
    assert element_section_where_to_h2.text == 'Weather forecasts, nowcasts and history in a fast and elegant way'

