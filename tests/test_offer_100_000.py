from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

URL = 'https://openweathermap.org/'

def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url

def test_open_page(driver):
    driver.get('https://openweathermap.org/%27')
    assert 'openweathermap' in driver.current_url
    print(driver.current_url)





