from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://openweathermap.org/"
load_div = (By.CSS_SELECTOR, 'div.owm-loader-container > div')
tab_guide = (By.CSS_SELECTOR, '#desktop-menu a[href="/guide"]')
tab_api = (By.CSS_SELECTOR, '#desktop-menu a[href="/api"]')
bt_go_home = (By.XPATH, "//a[contains(text(),'Home')]")


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
    tab_guild = WebDriverWait(driver, 45).until(EC.presence_of_element_located
                                                (tab_guide))
    tab_guild.click()
    assert driver.current_url == 'https://openweathermap.org/guide'
    bt_home = WebDriverWait(driver, 45).until(EC.presence_of_element_located
                                              (bt_go_home))
    bt_home.click()
    assert driver.current_url == URL
