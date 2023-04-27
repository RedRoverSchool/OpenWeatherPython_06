from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


def test_check_tab_blog(driver):
    driver.get('https://openweathermap.org/')
    tab_blog = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#desktop-menu li:nth-child(9) > a')))
    assert tab_blog.text == 'Blog'


