from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


def test_check_tab_blog(driver):
    driver.get('https://openweathermap.org/')
    tab_blog = driver.find_element(By.CSS_SELECTOR, '#desktop-menu li:nth-child(9)').text
    assert tab_blog == 'Blog'

