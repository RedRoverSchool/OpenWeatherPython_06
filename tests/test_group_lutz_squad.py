from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_go_to_blog(driver):
    driver.get('https://openweathermap.org/')
    WebDriverWait(driver, 10).until_not(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    go_to_blog = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#desktop-menu li:nth-child(9)')))
    go_to_blog.click()
    expected_page = 'https://openweather.co.uk/blog/category/weather'
    assert expected_page in driver.page_source