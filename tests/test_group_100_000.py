from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = 'https://openweathermap.org/'
def test_should_open_given_link(driver):
    driver.get(URL)
    assert 'openweathermap' in driver.current_url


def test_check_page_title(driver):
    # function checks page title
    driver.get('https://openweathermap.org')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'

def test_api_title1(driver):
    driver.get('https://openweathermap.org/')
    WebDriverWait(driver, 10).until_not(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.owm-loader-container > div')))
    button_nav_bar_api = WebDriverWait(driver, 35).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#desktop-menu>ul>li:nth-child(2)>a")))
    button_nav_bar_api.click()
    nav_bar_api_title_text = driver.find_element(By.CSS_SELECTOR, "h1[class]").text
    assert nav_bar_api_title_text == "Weather API"

