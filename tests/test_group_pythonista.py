from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://openweathermap.org/"
load_div = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
bt_go_home = (By.XPATH, "//a[contains(text(),'Home')]")
tab_guide = (By.XPATH, '//*[@id="desktop-menu"]/ul/li[1]/a')
tab_api = (By.XPATH, '//*[@id="desktop-menu"]/ul/li[2]/a')


def test_open_page(driver):
    driver.get('https://openweathermap.org/')
    driver.maximize_window()
    assert 'openweathermap' in driver.current_url


def test_check_page_title(driver):
    # function checks page title
    driver.get('https://openweathermap.org')
    assert driver.title == 'Сurrent weather and forecast - OpenWeatherMap'


def test_python():
    print('Hello girls!')


def test_checkout_menu_tab_guide(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    driver.find_element(*tab_guide).click()
    assert driver.current_url == 'https://openweathermap.org/guide'
    driver.find_element(*bt_go_home).click()
    assert driver.current_url == URL


def test_checkout_menu_tab_api(driver):
    driver.get(URL)
    wait = WebDriverWait(driver, 15)
    wait.until_not(EC.presence_of_element_located(load_div))
    driver.find_element(*tab_api).click()
    assert driver.current_url == 'https://openweathermap.org/api'
    driver.find_element(*bt_go_home).click()
    assert driver.current_url == URL
